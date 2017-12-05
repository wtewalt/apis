""" Functions


"""

# Import config.py
import config
import pandas as pd
from datetime import datetime, timedelta
from time import sleep

# Define functions
def get_report(analytics, start_date, end_date, view_id, metrics, dimensions, segments):
    """Queries the Analytics Reporting API V4.
    
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate':start_date, 'endDate': end_date}],
                    'metrics': metrics,
                    'dimensions': dimensions,
                    'pageSize': 10000,
                    'segments': segments
                }]
            }
    ).execute()


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

    Args:
    response: An Analytics Reporting API V4 response.
    """
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get(
            'metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                print(header + ': ' + dimension)

            for i, values in enumerate(dateRangeValues):
                print('Date range: ' + str(i))
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print(metricHeader.get('name') + ': ' + value)


def convert_response_to_df(response):
    list = []
    # get report data
    for report in response.get('reports', []):
        # set column headers
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
        rows = report.get('data', {}).get('rows', [])

        for row in rows:
            # create dict for each row
            dict = {}
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            # fill dict with dimension header (key) and dimension value (value)
            for header, dimension in zip(dimensionHeaders, dimensions):
                dict[header] = dimension

            # fill dict with metric header (key) and metric value (value)
            for i, values in enumerate(dateRangeValues):
                for metric, value in zip(metricHeaders, values.get('values')):
                    #set int as int, float a float
                    if ',' in value or ',' in value:
                        dict[metric.get('name')] = float(value)
                    else:
                        dict[metric.get('name')] = int(value)

            list.append(dict)

        df = pd.DataFrame(list)
        return df




#def return_ga_data(start_date, end_date, view_id, metrics, dimensions):
#    """ Combine the print_response and get_report functions."""
#    return convert_response_to_df(get_report(config.service, start_date, end_date, view_id, metrics, dimensions))

def return_ga_data(start_date, end_date, view_id, metrics, dimensions, segments, split_dates, group_by):
    if split_dates == False:
        return convert_response_to_df(get_report(config.service, start_date, end_date, view_id, metrics, dimensions, segments))
    else:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        delta = end_date - start_date         # timedelta
        dates = []

        for i in range(delta.days + 1):
            dates.append(start_date + timedelta(days=i))

        df_total = pd.DataFrame()
        for date in dates:
            date = str(date)
            df_total = df_total.append(convert_response_to_df(get_report(
                config.service, date, date, view_id, metrics, dimensions, segments)))
            sleep(1)

        if len(group_by) != 0:
            df_total = df_total.groupby(group_by).sum()

        return df_total


def clean_column_list(x):
    """ Remove the source from a list of column names.
    
    All google analytics col headers include the string 'ga:'
    However, some special sources are removed first if they exist in the column name.
    Finally, 
    """
    special_source_list = ['ga:dcm', 'ga:adsense', 'ga:adx', 'ga:dfp', 'ga:backfill',
                           'ga:ds', 'ga:dbm']
    for source in special_source_list:
        x= x.replace(source, '')
    if x[:3]== 'ga:':
        x= x.replace('ga:', '')
    return x


def clean_df_columns(df):
    """ Clean and replace column names

    Uses clean_column_list() to create new column names.
    Columns in the df are then replaced with the new names.
    """
    col_list = list(df.columns.values)
    new_columns = [clean_column_list(col) for col in col_list]
    df.columns = new_columns
    return df

def format_date(x):
    new_x = datetime.strptime(x, '%Y%m%d').strftime('%Y-%m-%d')
    return new_x

def format_all_dates(x):
    separated_dates = [format_date(d) for d in x]
    return separated_dates
    