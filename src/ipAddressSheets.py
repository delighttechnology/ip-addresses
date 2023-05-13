import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

# prage that retrives the external IP address
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# oAuth scopes used by Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

# address to the JSON Key genereted by API for ServiceAccount
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Andrzej\\Documents\\Python\\ip_addresses\\ipaddresses-f1c86666378c.json", scopes=SCOPES)
file = gspread. authorize (creds)
sheet = file.open("ip_addresses")
sheet = sheet.sheet1

# row insert
insertRow = [date,time,external_ip]
sheet.insert_row([' '], index=2)
sheet.append_row(insertRow,value_input_option="USER_ENTERED", table_range="A2:C2")


