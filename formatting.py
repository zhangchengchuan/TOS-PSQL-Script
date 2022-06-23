from pprint import *

def format_trade(trade):
    try:
        date = trade['settlementDate']
        total = trade['netAmount']

        item = trade['transactionItem']
        quantity, price, buysell = item['amount'], item['price'], item['instruction']
        ticker, asset, cusip = item['instrument']['symbol'], item['instrument']['assetType'], item['instrument']['cusip']

        # print(trade)
        return [ticker, asset, buysell, quantity, price, total, cusip, date] 
    except:
        return 


def format_account_info(acc_info):
    try:
        # pprint(acc_info['securitiesAccount']['initialBalances']['accountValue'])
        value = acc_info['securitiesAccount']['initialBalances']['accountValue']
        cash = acc_info['securitiesAccount']['currentBalances']['cashBalance']
        margin = acc_info['securitiesAccount']['initialBalances']['margin']
        long = acc_info['securitiesAccount']['currentBalances']['longMarketValue']
        short = acc_info['securitiesAccount']['currentBalances']['shortMarketValue']

        # print(value)
        return [value, cash, margin, long, short]

    except:
        return



