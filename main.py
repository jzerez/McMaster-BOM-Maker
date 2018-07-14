from McMasterSelenium import scrape
import gspread
import os.path
import time
from oauth2client.service_account import ServiceAccountCredentials

VENDOR_COL = 2
PART_NUM_COL = 3
DESC_COL = 4
NUM_NEEDED_COL = 5
NUM_PER_UNIT_COL = 6
UNITS_NEEDED_COL = 7
PRICE_PER_UNIT_COL = 8
TOTAL_PRICE_COL = 9
#WRITE_COLS = [DESC_COL, NUM_PER_UNIT_COL, UNITS_NEEDED_COL, PRICE_PER_UNIT_COL, TOTAL_PRICE_COL]
WRITE_COLS = [DESC_COL, NUM_PER_UNIT_COL, PRICE_PER_UNIT_COL]
READ_COLS = [PART_NUM_COL, NUM_NEEDED_COL]

def update_cell(sheet, row, col, info):
    if info != 'N/A':
        sheet.update_cell(row, col, info)
        time.sleep(0.011)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

assert os.path.isfile('client_secret.json'), "API private authentication missing."
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Copy of Brakes and Pedals').sheet1

for row_id, vendor in enumerate(sheet.col_values(2)):
    needs_scraping = False
    update_possible = False
    part_num = None
    num_needed = None
    if "mcmaster" in vendor.lower():
        curr_row = sheet.row_values(row_id + 1)
        for col_id, elem in enumerate(curr_row):
            if ((col_id + 1) in WRITE_COLS) and not elem:
                needs_scraping = True

            if ((col_id + 1) == PART_NUM_COL) and elem:
                update_possible = True
                part_num = elem

            if ((col_id + 1) == NUM_NEEDED_COL) and elem:
                update_possible = True
                num_needed = elem

        if needs_scraping and update_possible:
            print(part_num)
            part_info = scrape(part_num)
            update_cell(sheet, row_id + 1, DESC_COL, part_info['name'])
            update_cell(sheet, row_id + 1, NUM_PER_UNIT_COL, part_info['#_per_unit'])
            update_cell(sheet, row_id + 1, PRICE_PER_UNIT_COL, part_info['price_per_unit'])
        else:
            print('needs_scraping? ', needs_scraping)
            print('update_possible? ', update_possible)
