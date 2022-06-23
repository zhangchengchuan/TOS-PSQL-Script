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
from formatting import format_account_info, format_trade, format_account_info

def main():
    # access.login()
    # connection, cursor = access.logindb()

####################################################################################################################################

# # Fetch account details
    # Current account value - Store First value as initial capital
    acc_info = api_call("ACCOUNT_INFO")
    entry = format_account_info(acc_info)
    insert_query = f'''
    INSERT INTO account_info()
    '''

####################################################################################################################################



#     # Past Trades
#     past_trades = api_call("TRANSACTIONS")
    
#     for trade in past_trades:
#         if trade['type'] == "TRADE":
#             entry = format_trade(trade)
#             insert_query = f'''
#             INSERT INTO past_trades(ticker, asset, buysell, quantity, price, total, cusip, date)
#             VALUES ('{entry[0]}', '{entry[1]}', '{entry[2]}', {entry[3]}, {entry[4]}, {entry[5]}, '{entry[6]}', '{entry[7]}')
#             '''
#             # if cusip already exists, then dont add to database

#             cursor.execute(insert_query)
#             connection.commit()
#             return 



#     # Open positions and metadata - Ticker, Name, Average, Last Price, Quantity, % of capital

####################################################################################################################################

    # TRANSACTION HISTORY

    # Getting pickle first
    
    # past_trades = api_call("TRANSACTIONS")
    # pickled_trades = open("trades.pkl", "wb")
    # pickle.dump(past_trades, pickled_trades)
    # pickled_trades.close()
    
    # # [ticker, asset, buysell, quantity, price, total, cusip6, date7] 

    # pickled_trades = pickle.load(open("trades.pkl","rb"))
    # cusip_list = {}
    # close = {}
    # opened = {}
    # for trade in pickled_trades[::-1]:
    #     formatted_trade = format_trade(trade)
    #     if formatted_trade is None:
    #         pass
    #     else:
    #         cusip = formatted_trade[6]
    #         quantity  = formatted_trade[3] if formatted_trade[2] == "BUY" else -1 * formatted_trade[3]
    #         if cusip not in cusip_list:
    #             cusip_list[cusip] = quantity
    #             opened[cusip] = quantity
    #         else:
    #             val = cusip_list[cusip]
    #             new_val = val + quantity
    #             if new_val == 0:
    #                 opened.pop(cusip)
    #                 close[cusip] = 1 # there is transaction of this cusip closed
    #             else:
    #                 opened[cusip] = new_val

    # pprint(opened)
    # pprint(close)

####################################################################################################################################

# Fetch ticker and index symbols

    # Clean up connections
    # cursor.close()
    # connection.close()


if __name__ == '__main__':
    main()