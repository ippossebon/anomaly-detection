#!/usr/bin/python
import json
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

def main():
    print('Main')


    json_key = json.load(open('client_secret.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = oauth2client.client.SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    sht1 = gc.open_by_key('12ApHICacHZfqvUv7xMwcFf9z8slM4vSAmOv4AyEMONk')
    # With label
    val = sht1.acell('B1').value
    print(val)
    print('fim')
    #wks.update_acell('B2', "it's down there somewhere, let me take another look.")

    # Fetch a cell range
    #cell_list = wks.range('A1:B7')



def read_dict_file(file_name):
    s = open(file_name, 'r').read()
    data_dict = ast.literal_eval(s)
    print(data_dict)


if __name__ == '__main__':
    main()
