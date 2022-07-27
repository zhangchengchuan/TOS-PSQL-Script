import psycopg2 as pg
import requests
import webbrowser
import urllib
import time
import psycopg2
import pickle 
from pprint import *

import edit_json
import access
from api import api_call
from formatting import format_account_info, format_trade, format_account_info, organize_trades

def main():
    connection, cursor = access.logindb()

####################################################################################################################################

# # Fetch account details
    # Current account value - Store First value as initial capital
    # acc_info = format_account_info(api_call("ACCOUNT_INFO"))
    # pprint(acc_info[0])
    # entry = format_account_info(acc_info)
    # insert_query = f'''
    # INSERT INTO account_info()
    # '''

####################################################################################################################################

# Fetch ticker and index symbols

    api_call("WATCHLIST")

####################################################################################################################################
    # Clean up connections
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()