import requests
from requests.structures import CaseInsensitiveDict
import json
import os

url = os.environ['SLACK_WEBHOOK_URL']
acm_url = os.environ['ACM_URL']

print(url[0:10])
print(acm_url[0:10])

# attachments
A1 = os.environ.get('A1', 'https://www.redhat.com')
A2 = os.environ.get('A2', 'https://www.redhat.com')

channel = '#team-acm-alertmanager-stage'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

ACM='`2.6.0-DOWNSTREAM-2022-07-13-23-23-00`'
MCE='`2.6.0-DOWNSTREAM-2022-07-13-23-23-00`'
SPRINT=13
IDP_VERSION = "0.3.3"
OCP_VERSION = "4.10.13"

# text format
S="\n> RHACM - Sprint " + str(SPRINT)
U="\n> URL: " + acm_url
I="\n> IDP-MGMT-CONFIG: " + IDP_VERSION
O="\n> OCP version: " + "`" + OCP_VERSION + "`"
F="\n> See this doc for environment details:"
T="> *2.6.0 Playback Demo Clusters Available!* :rocket:" + S + U + "\n> ACM: " + ACM + "\n> MCE: " + MCE + I + O

data_raw = {
    "text": T,
    "attachments": [
        {
            "title": "Deployment Details",
            "title_link": A1
        },
        {
            "title": "Pod Listing",
            "title_link": A2
        }
    ]
}

# data_raw = {
#     "text": T,
#     "blocks": [
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": T
#             }
#         },
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": A1
#             }
#         },
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": A2
#             }
#         }
#     ]
# }

resp = requests.post(url, headers=headers, data=json.dumps(data_raw))

print(resp.status_code)
