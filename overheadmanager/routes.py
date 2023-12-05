from flask import render_template, request
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
    return render_template("reports.html", bar_data=[{'x': sectors, 'y': total, 'type': 'bar'}])


@app.route("/timesheets")
def timesheets():
    november = SHEET.worksheet('November')
    values = november.get_all_values()
    sectors = [value[0] for value in values[1:]]
    employees = values[0][1:12]
    return render_template("timesheets.html", sheet_data={'sectors': sectors, 'employees': employees})


@app.route("/view_timesheet", methods=["GET", "POST"])
def add_timesheet():
    print(request.form)
    november = SHEET.worksheet('November')
    values = november.get_all_values()
    sectors = [value[0] for value in values[1:]]
    employees = values[0][1:12]
    selected_employee_index = employees.index(request.form['employee']) + 2
    selected_sector_index = sectors.index(request.form['sector']) + 2
    print(f"selected_employee_index {selected_employee_index} - selected_sector_index {selected_sector_index}")
    november.update_cell(selected_sector_index, selected_employee_index, request.form['hours']) 
    return render_template("view_timesheet.html")