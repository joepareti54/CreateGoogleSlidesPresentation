from __future__ import print_function
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
import pandas as pd
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
SCOPES = 'https://www.googleapis.com/auth/drive'
#
def do_createSlide_insertImage(service, XXX, image, index, drive, slides):
  requests = [
{
     'createSlide': {
     'insertionIndex': '1',
     'slideLayoutReference': {
     'predefinedLayout': 'TITLE_AND_TWO_COLUMNS'
             }
         }
     }
               ]
  body1 = { 'requests': requests}
#
  response = service.presentations() \
  .batchUpdate(presentationId=XXX, body=body1).execute()
  create_slide_response = response.get('replies')[0].get('createSlide')
  print('Created slide with ID: {0}'.format(
  create_slide_response.get('objectId')))
  YYY = create_slide_response.get('objectId')
#
  uploadFilename = image  # Please set the filename with the path.
  presentation_id = XXX  # Please set the Google Slides ID.
  pageObjectId = YYY  # Please set the page ID of the Slides.


# 1. Upload a PNG file from local PC
  file_metadata = {'name': uploadFilename}
  media = MediaFileUpload(uploadFilename, mimetype='image/png')
#print(file_metadata)
#print(media)
  upload = drive.files().create(body=file_metadata, media_body=media, fields='webContentLink, id, webViewLink').execute()
  fileId = upload.get('id')
  url = upload.get('webContentLink')
  drive.permissions().create(fileId=fileId, body={'type': 'anyone', 'role': 'reader'}).execute()
  body = {
    "requests": [
        {
            "createImage": {
                "url": url,
                "elementProperties": {
                    "pageObjectId": pageObjectId
                }
            }
        }
    ]
}
  slides.presentations().batchUpdate(presentationId=presentation_id, body=body).execute()


#----------------MAIN --------------------------
#
creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

service = build('slides', 'v1', credentials=creds)

title = 'JP_february13-2021 '
body0 = {'title': title}

drive = build('drive', 'v3', credentials=creds)
slides = build('slides', 'v1', credentials=creds)
#
presentation = service.presentations().create(body=body0).execute()
print('Created presentation with ID: {0}'.format(
presentation.get('presentationId')))
XXX = presentation.get('presentationId')
df = pd.read_csv('files',header = None)
df.columns = ['file_name']
LI = df['file_name'].tolist()
l_LI = len(LI)
#    print('length ',l_LI)
for i in range(l_LI):
      index = i+1
      image  = LI[i]
      do_createSlide_insertImage(service, XXX, image, index, drive, slides)

