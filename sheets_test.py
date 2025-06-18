import gspread
from google.oauth2.service_account import Credentials

# Path to your downloaded credentials
CREDENTIALS_FILE = r'C:\Users\Admin Lenovo\Documents\Coding\Python\credentials.json'

# Scopes define the access level
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authorize the client
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open_by_key("1-p_GJztVfyDPzvKBEJd2kzlD3UVRee2sZPM-KV3RymE").sheet1

# Sample data to insert
row = ["John Doe", "john@example.com", "Mathematics"]

# Append the data to the sheet
sheet.append_row(row)

print("✅ Data written to Google Sheet successfully.")