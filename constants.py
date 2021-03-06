""" This file holds some of the constants used in run.py

Included:
* View IDs
* Segment IDs
* GA dimensions
* GA metrics
* start and end dates

These will help us stay consistent across all queries
"""


SESSIONS_METRICS = [
    {'expression': 'ga:sessions'},
    {'expression': 'ga:users'},
    {'expression': 'ga:newUsers'},
    {'expression': 'ga:bounces'},
    {'expression': 'ga:pageviews'},
    {'expression': 'ga:uniquePageviews'},
    #{'expression': 'ga:goalCompletionsAll'},
    #{'expression': 'ga:goal1Completions'},
    #{'expression': 'ga:goal2Completions'},
    #{'expression': 'ga:goal3Completions'},
    #{'expression': 'ga:goal4Completions'},
    #{'expression': 'ga:goal5Completions'},
]

SESSIONS_DIMENSIONS = [
    {'name': 'ga:sourceMedium'},
    {'name': 'ga:segment'},  # segment dim can't be removed
    {'name': 'ga:date'},
    {'name': 'ga:keyword'},
    {'name': 'ga:campaign'},
    {'name': 'ga:pagePath'},
    #{'name': 'ga:adContent'},
    #{'name': 'ga:deviceCategory'},
    {'name': 'ga:metro'}
]

SEGMENTS = [{"segmentId": "gaid::-1"}]


# View IDs
VIEW_ID= ''

""" Dates

[TODO]
* Dynamically calculate start and end dates
* End Date is today - 1
* Start Date needs to consider that historical data can change...?
    ^ What about always remove the last 30 days and then append?
"""

START_DATE= '2017-12-01'
END_DATE= '2017-12-10'

