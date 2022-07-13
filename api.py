import requests
import time
import datetime

from edit_json import read_json, change_json_file

def api_call(call_type):

    config = read_json('config.json')

    # Always get the new access token first    
    # print("Refresh Token still valid. Access Token refreshed.")
    r = requests.post(r'https://api.tdameritrade.com/v1/oauth2/token',
                        headers={
                            "Content-Type": "application/x-www-form-urlencoded"
                        },
                        data={
                            'grant_type': 'refresh_token',
                            'refresh_token': config['refreshToken'],
                            'access_type': 'offline',
                            'client_id': config['clientID'],
                        })
    response = r.json()
    config['refreshToken'] = response['refresh_token']
    config['accessToken'] = 'Bearer ' + response['access_token']

    # Time Stamp in time since epoch
    config['timeStamp'] = time.time()

    # Save changes to json file
    change_json_file('config.json', config)


####################################################################################################################################

    if call_type == "ACCOUNT_INFO":
        s = f'https://api.tdameritrade.com/v1/accounts'
        # s = f'https://api.tdameritrade.com/v1/accounts/{config["accountNumber"]}'
        r = requests.get(s,
                    headers={
                        "Authorization": config['accessToken']
                    })
        
        return r.json()
    
    elif call_type == "TRANSACTIONS":
        date_today = datetime.datetime.today().strftime('%Y-%m-%d')
        s = f'https://api.tdameritrade.com/v1/accounts/{config["accountNumber"]}/transactions'
        r = requests.get(s,
                    headers={
                        "Authorization": config['accessToken']
                    },
                    params={
                        'type': "TRADE",
                        'startDate': config['prevDate'],
                        'endDate': date_today,
                    })
        
        # Comment out for testing purpose. Uncomment when ready to deploy

        # # Update the prev date to today so don't have to query entire transaction history
        # config['prevDate'] = date_today
        # change_json_file('config.json', config)

        return r.json()





