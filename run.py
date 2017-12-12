""" Query google analytics core reporting API v4.

The query must be built below.
View IDs come from the google analytics online interface settings.
Segment IDs come from the following address:
    https://ga-dev-tools.appspot.com/query-explorer/

Metrics and Dimensions:
    https://developers.google.com/analytics/devguides/reporting/core/dimsmets#cats=user,session,traffic_sources,adwords,goal_conversions,platform_or_device,geo_network,system,social_activities,page_tracking,content_grouping,internal_search,site_speed,app_tracking,event_tracking,ecommerce,social_interactions,user_timings,exceptions,content_experiments,custom_variables_or_columns,time,doubleclick_campaign_manager,audience,adsense,ad_exchange,doubleclick_for_publishers,doubleclick_for_publishers_backfill,lifetime_value_and_cohorts,channel_grouping,related_products,doubleclick_bid_manager,doubleclick_search

"""

from functions import return_ga_data, clean_df_columns, format_all_dates
import constants



# get sessions data.


#
#
#
# CSpire
#
#
#
#
"""
cspire_sessions_df = return_ga_data(
    START_DATE='2017-11-30',
    end_date='2017-11-30',
    view_id=constants.CSPIRE_VIEW_ID,
    metrics=constants.SESSIONS_METRICS,
    dimensions=constants.SESSIONS_DIMENSIONS,
    segments=constants.CSPIRE_SEGMENTS,
    split_dates=True,
    group_by=[]
)

# Rename columns
cspire_sessions_df = clean_df_columns(cspire_sessions_df)

if 'date' in cspire_sessions_df: 
    cspire_sessions_df['date'] = format_all_dates(cspire_sessions_df.date)
"""
#
#
#
#
# Salsaritas
#
#
#
#
salsaritas_sessions_df = return_ga_data(
    start_date=constants.START_DATE,
    end_date=constants.END_DATE,
    view_id=constants.SALSARITAS_VIEW_ID,
    metrics=constants.SESSIONS_METRICS,
    dimensions=constants.SESSIONS_DIMENSIONS,
    segments=constants.SALSARITAS_SEGMENTS,
    split_dates=True,
    group_by=[]
)

# Rename columns
salsaritas_sessions_df = clean_df_columns(salsaritas_sessions_df)

if 'date' in salsaritas_sessions_df:
    salsaritas_sessions_df['date'] = format_all_dates(salsaritas_sessions_df.date)





""" Viewing some results

Check that all requested dimensions and metrics are returned.
Print the df shape to get a sense of rows per day returned.
"""

print(salsaritas_sessions_df[:10]) # cspire_sessions_df[:4]
print(salsaritas_sessions_df.shape)
#salsaritas_sessions_df.to_csv('W:/Clients/Salsarita\'s/Analytics - Salsa\'s/Weekly Reporting/Website Tracking/ga_salsaritas_pageviews.csv')



""" Creating the Pages-level Query

pages_df = return_ga_data(
    START_DATE='2017-09-20',
    end_date='2017-09-20',
    view_id=  '84446473',
    metrics=[{'expression': 'ga:sessions'},
             {'expression': 'ga:users'},
             {'expression': 'ga:newUsers'},
             {'expression': 'ga:bounces'}, ],
    dimensions=[{'name': 'ga:date'},
                #{'name': 'ga:hostname'},
                #{'name': 'ga:pagePath'},
                {'name': 'ga:pageTitle'},
                {'name': 'ga:landingPagePath'},
                {'name': 'ga:exitPagePath'}],
    split_dates=True,
    group_by=[]
)

pages_df = clean_df_columns(pages_df)
pages_df['date'] = format_all_dates(pages_df.date)
print(pages_df[:4])
print(pages_df.shape)
"""
