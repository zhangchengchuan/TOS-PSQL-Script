from pprint import *
from api import api_call

# for testing
import pickle

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

def organize_trades(prev_trades, new_trades: dict) -> list:
    open = prev_trades[0] # cusip: [quantity, [list of trades]]
    close = prev_trades[1] # cusip: [list of closed trades]
    cusip_list = prev_trades[2] # cusip: quantity

    trades = list(map(format_trade, new_trades))

    for trade in trades:
        cusip = trade[0]
        quantity  = trade[3] if trade[2] == "BUY" else -1 * trade[3]
        if cusip not in cusip_list:
            cusip_list[cusip] = quantity
            open[cusip] = []
            open[cusip].append(trade)
        else:
                open[cusip].append(trade)
                new_val = cusip_list[cusip] + quantity
                
                # Quantity netted out to 0 -> Update close list
                if new_val == 0:
                    if cusip not in close:
                        close[cusip] = open[cusip]
                    else:
                        close[cusip].extend(open[cusip])

                    # reset the current open list and reset current count
                    open[cusip] = []
                    cusip_list[cusip] = 0
                else:
                    cusip_list[cusip] = new_val

    # pprint(cusip_list)
    # pprint(close)
    # pprint(open)

    return open, close, cusip_list


# # For testing
# pickled_trades = pickle.load(open("trades.pkl", 'rb'))
# organize_trades(pickled_trades)

