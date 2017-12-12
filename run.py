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


#
#
#
#
# Do Stuff
#
#
#
#
sessions_df = return_ga_data(
    start_date=constants.START_DATE,
    end_date=constants.END_DATE,
    view_id=constants.VIEW_ID,
    metrics=constants.SESSIONS_METRICS,
    dimensions=constants.SESSIONS_DIMENSIONS,
    segments=constants.SEGMENTS,
    split_dates=True,
    group_by=[]
)

# Rename columns
sessions_df = clean_df_columns(sessions_df)

if 'date' in sessions_df:
    sessions_df['date'] = format_all_dates(sessions_df.date)

