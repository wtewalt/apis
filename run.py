""" Query google analytics core reporting API v4.

The query must be built below.
View IDs come from the google analytics online interface settings.
Segment IDs come from the following address:
    https://ga-dev-tools.appspot.com/query-explorer/

Metrics and Dimensions:
    https://developers.google.com/analytics/devguides/reporting/core/dimsmets#cats=user,session,traffic_sources,adwords,goal_conversions,platform_or_device,geo_network,system,social_activities,page_tracking,content_grouping,internal_search,site_speed,app_tracking,event_tracking,ecommerce,social_interactions,user_timings,exceptions,content_experiments,custom_variables_or_columns,time,doubleclick_campaign_manager,audience,adsense,ad_exchange,doubleclick_for_publishers,doubleclick_for_publishers_backfill,lifetime_value_and_cohorts,channel_grouping,related_products,doubleclick_bid_manager,doubleclick_search

"""

from functions import return_ga_data, clean_df_columns, format_all_dates

# get data

""" Notes


** View IDs **

Note: View IDs are used as strings in the code below.

www.cspire.com = '84446473'
    * Business-only = '141075452'
Credera = '146168974'
Home Service = '154585144'
Home Services(Legacy)= '141114926'
Prepaid = '159884119'
Raw Data = '84454783'
Wireless 04282017 = '149218469'
Wireless Only = '141562611'



** Data to add **

Sesions Data:
    new users [DONE]
    users [DONE]
    sessions [DONE]
    session duration
    bounces [DONE]
    source [DONE]
    medium [DONE]
    campaign [DONE]
    ad-content [DONE]
    keyword [DONE]
    goal completions(1-6?)

"""



# get sessions data.

sessions_df = return_ga_data(
    start_date='2017-11-30',
    end_date='2017-11-30',
    view_id='84446473',
    metrics=[{'expression': 'ga:sessions'}, 
             {'expression': 'ga:users'}, 
             #{'expression': 'ga:newUsers'},
             #{'expression': 'ga:bounces'},
             #{'expression': 'ga:goalCompletionsAll'},
             #{'expression': 'ga:goal1Completions'},
             #{'expression': 'ga:goal2Completions'},
             #{'expression': 'ga:goal3Completions'},
             #{'expression': 'ga:goal4Completions'},
             #{'expression': 'ga:goal5Completions'}, 
             ],
    dimensions=[{'name': 'ga:sourceMedium'},
                {'name': 'ga:segment'},
                {'name': 'ga:date'}
                #{'name': 'ga:keyword'},
                #{'name': 'ga:campaign'},
                #{'name': 'ga:referralPath'},
                #{'name': 'ga:adContent'},
                #{'name': 'ga:userType'},
                #{'name': 'ga:deviceCategory'}
                ],
    segments=[{"segmentId": "gaid::GvB1BxZNQDGKw3i3JTzBZw"}, # Business
              {"segmentId": "gaid::h7S_Jb8iS_aPbQjsbKnJzw"}, # Consumer
              {"segmentId": "gaid::-1"} # All Users
              ],
    split_dates=True,
    group_by=[]
)

# Rename columns
sessions_df = clean_df_columns(sessions_df)

if 'date' in sessions_df: 
    sessions_df['date'] = format_all_dates(sessions_df.date)



""" Viewing some results

Check that all requested dimensions and metrics are returned.
Print the df shape to get a sense of rows per day returned.
"""

# print(sessions_df[:10]) # sessions_df[:4]
# print(sessions_df.shape)
# sessions_df.to_csv('c:/Users/wtewalt/Documents/ga_biweekly_data.csv')



""" Creating the Pages-level Query

pages_df = return_ga_data(
    start_date='2017-09-20',
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
