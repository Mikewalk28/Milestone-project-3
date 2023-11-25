# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
from overheadmanager import app
import gspread
from google.oauth2.service_account import Credentials

#if __name__ == "__main__":
     # app.run(
      #  host=os.environ.get("IP"),
        #port=int(os.environ.get("PORT")),
      #  debug=os.environ.get("DEBUG")
  #  )

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