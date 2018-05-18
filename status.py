import gspread
from oauth2client.service_account import ServiceAccountCredentials



def checking():
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
  gc = gspread.authorize(credentials)
  wks = gc.open('Kurusaki_database_discord').time
  ald=wks.get_all_records()
  print(ald)
