""" Credentials file

Instructions followed here:
https://www.themarketingtechnologist.co/getting-started-with-the-google-analytics-reporting-api-in-python/

Contains the credentials needed to connect to the google analytics API.
Connections to GA go through the SEM@johngroup.com login
 
"""

import json

# Get credentials file
with open('ga_creds.json') as j:
    creds= json.load(j)


client_id = creds['client_id']
client_secret = creds['client_secret']
redirect_uri = creds['redirect_uri']
access_code = creds['access_code']
access_token = creds['access_token']
refresh_token = creds['refresh_token']

