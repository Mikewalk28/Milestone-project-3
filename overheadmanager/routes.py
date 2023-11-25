from flask import render_template
from overheadmanager import app, db
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Milestone-project-3')

fy21 = SHEET.worksheet('FY21/22')
january = SHEET.worksheet('January')

data = fy21.get_all_values()
data2 = january.get_all_values()

print(data)
print(data2)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reports")
def reports():
    fy21 = SHEET.worksheet('FY21/22')
    data = fy21.get_all_values()
    return render_template("reports.html", sheet_data=data)
