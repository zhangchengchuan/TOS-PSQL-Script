from pprint import *
from api import api_call

def format_trade(trade: dict) -> list:
    try:
        date = trade['settlementDate']
        total = trade['netAmount']

        item = trade['transactionItem']
        quantity, price, buysell = item['amount'], item['price'], item['instruction']
        ticker, asset, cusip = item['instrument']['symbol'], item['instrument']['assetType'], item['instrument']['cusip']

        return [ticker, asset, buysell, quantity, price, total, cusip, date] 
    except:
        return 


def format_account_info(acc_info) -> list:
    try:
        acc_info = acc_info[0] # First index is main account. This is here because error with accounts API -- accounts/<acc_no> doesnt work but accounts/ works.
        value = acc_info['securitiesAccount']['currentBalances']['liquidationValue']
        cash = acc_info['securitiesAccount']['currentBalances']['cashBalance']
        margin = acc_info['securitiesAccount']['initialBalances']['margin']
        long = acc_info['securitiesAccount']['currentBalances']['longMarketValue']
        short = acc_info['securitiesAccount']['currentBalances']['shortMarketValue']

        return [value, cash, margin, long, short]

    except:
        return

def organize_trades(trades: dict) -> list:
    open = dict() # cusip: [quantity, [list of trades]]
    close = dict() # cusip: [list of closed trades]
    cusip_list = dict() # cusip: quantity

    trades = list(map(format_trade, trades))

    for trade in trades:
        cusip = trade[6]
        quantity  = trade[3] if trade[2] == "BUY" else -1 * trade[3]
        if cusip not in cusip_list:
            cusip_list[cusip] = quantity


    return trades

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


