import gspread
from oauth2client.service_account import ServiceAccountCredentials




scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Kurusaki_database_discord').sheet2



