
import psycopg2 as pg
import requests
import webbrowser
import urllib
import time
import psycopg2
import pickle
import time
import datetime
from pprint import *

import access
from api import api_call
from formatting import format_account_info, format_trade, format_account_info
from edit_json import read_json, change_json_file


def main():
    connection, cursor = access.logindb()

    ####################################################################################################################################
    # Update of current information


    # TD API to get newest acc info
    acc_info = format_account_info(api_call("ACCOUNT_INFO"))

    # Get previous "current info" first to compare maxdrawdown and highwater
    cursor.execute("SELECT * FROM current_information;")
    prev = cursor.fetchone()
    new_highwater = max(acc_info[0], prev[6]) 
    new_max_drawdown = ((new_highwater - acc_info[0])/acc_info[0]) * 100

    # Delete previous "current info"
    cursor.execute("""
        TRUNCATE current_information;
        """)
    connection.commit()

    # Insert
    cursor.execute("""
        INSERT INTO current_information (value, cash, margin, long_value, short_value, highwater, max_drawdown)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, 
        (acc_info[0], acc_info[1], acc_info[2], acc_info[3], acc_info[4], new_highwater, new_max_drawdown))
    connection.commit()




    ####################################################################################################################################
    # Update of equity curve -> Updates between 10PM and 11PM UTC time

    
    config = read_json('config.json')
    updated = config['dailyUpdate']
    current_hour = datetime.datetime.now().hour
    current_date = datetime.datetime.now().date()

    if current_hour <= 11 and current_hour >= 10:
        if not updated:
            # Get previous values
            cursor.execute("""
                SELECT * FROM account_values ORDER BY id DESC LIMIT 1;
                """)  
            prev = cursor.fetchone()
            percent_change = ((acc_info[0] - prev[2]) / prev[2]) * 100
            absolute_change = acc_info[0] - prev[2]

            cursor.execute("""
                INSERT INTO account_values (date, account_value, percent_change, absolute_change)
                VALUES (%s, %s, %s, %s);
                """,
                (current_date, acc_info[0], percent_change, absolute_change))
            connection.commit()

            # Change flag to 1 after updating
            config['dailyUpdate'] = 1
            change_json_file('config.json', config)

        else:
            # Already updated
            pass
        
    else:
        # Not time to update the daily values yet, but change the flag, so ready to update when 6AM comes.
        config['dailyUpdate'] = 0
        change_json_file('config.json', config)




    ####################################################################################################################################
    # Open positions and metadata - Ticker, Name, Average, Last Price, Quantity, % of capital
    # Fetch ticker and index symbols




    ####################################################################################################################################
    # Clean up connections and print updates
    cursor.close()
    connection.close()
    print(f'Routine update complete at {datetime.datetime.now()}')

if __name__ == "__main__":
    main()
