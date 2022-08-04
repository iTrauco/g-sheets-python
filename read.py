#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json' 

#.config/gspread/service_account.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FSbRZ2-R7ZMrE79N3hlTlpHZs2AqsaJSUW-a9qRciSg'
SAMPLE_RANGE_NAME = 'Projects!L13:L'



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()

values = result.get('values', [])

aoa = [[1,2,3,4],[5,6,7,8]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Tests!B2", 
                                valueInputOption="USER_ENTERED", 
                                body={"values":aoa}).execute()

print(request)
##if not values:
#    print('No data found.')
#    return
#
#print('Name, Major:')
#for row in values:
#    # Print columns A and E, which correspond to indices 0 and 4.
#    print('%s, %s' % (row[0], row[4]))
#                except HttpError as err:
#                    print(err)
#
#
