# Get Access Token.
import time
import urllib
import webbrowser
import requests
import psycopg2

from edit_json import read_json, change_json_file


def logindb():
    config = read_json("config.json")
    connection = psycopg2.connect(
        host=config['host'],
        database= config['database'],
        port=config['port'],
        user=config['user'],
        password=config['password']
    )

    cursor = connection.cursor()
    return connection, cursor

# def account():
#     
# 
# 
# 

