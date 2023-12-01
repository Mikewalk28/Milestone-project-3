from flask import render_template
from overheadmanager import app, db
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Milestone-project-3')

fy22 = SHEET.worksheet('FY22/23')
november = SHEET.worksheet('November')

data = fy22.get_all_values()
data2 = november.get_all_values()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/reports")
def reports():
    fy22 = SHEET.worksheet('FY22/23')
    headers = ["Sector", "Total"]
    values = fy22.get_all_values()
    sectors = [value[0] for value in values[1:]]
    total = [value[12] for value in values[1:]]
    return render_template("reports.html", sheet_data=[sectors, total])


@app.route("/reports-data")
def reports_data():
    fy22 = SHEET.worksheet('FY22/23')
    headers = ["Sector", "Total"]
    values = fy22.get_all_values()
    sectors = [value[0] for value in values[1:]]
    total = [value[12] for value in values[1:]]
    return render_template("reports.html", bar_data=[{'x': sectors, 'y': total, 'type': 'bar'}])


@app.route("/timesheets")
def timesheets():
    november = SHEET.worksheet('November')
    data = november.get_all_values()
    return render_template("timesheets.html", sheet_data=data)