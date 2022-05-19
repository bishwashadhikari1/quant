from cmath import e
import time
from typing import final
from core import session
from positioncheck import order_list
from tickers import list_of_tickers

# session.futures_get_open_orders()
# session.futures_change_leverage(symbol='ETHUSDT', leverage=15)
# session.futures_create_order(
#     symbol='ETHUSDT',
#     quantity=0.02,
#     type='LIMIT',
#     side='SELL',
#     timeInForce= 'GTC',
#     price=2098.42
#     )

def precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide):
    actual_order = session.futures_create_order(
        symbol=tick,
        side=side,
        positionSide=pSide,
        quantity=positionsize,
        type='LIMIT',
        timeInForce= 'GTC',
        price=entry,
        )
    stop_order = session.futures_create_order(
        side=diee,
        positionSide=pSide,
        symbol=tick,
        type='STOP_MARKET',
        timeInForce= 'GTC',
        stopPrice=sl,
        quantity = positionsize
        )
    prof_order = session.futures_create_order(
        side=diee,
        positionSide=pSide,
        symbol=tick,
        type='TAKE_PROFIT_MARKET',
        timeInForce= 'GTC',
        stopPrice=tp,
        quantity = positionsize
        )
    pId=prof_order['orderId']
    sId=stop_order['orderId']
    oId=actual_order['orderId']
    
    return [pId, sId,oId]



def order(tick, positionsize, side, diee, entry, tp, sl, pSide):
    try:
        return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide)
    except:
        try:
            positionsiz= "{:.3f}".format(positionsize)
            positionsize=float(positionsiz)
            tpp= "{:.3f}".format(tp)
            tp=float(tpp)
            sll= "{:.3f}".format(sl)
            sl=float(sll)            
            return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide)
        except:
            try:
                tpp= "{:.2f}".format(tp)
                tp=float(tpp)
                sll= "{:.2f}".format(sl)
                sl=float(sll) 
                positionsiz= "{:.2f}".format(positionsize)
                positionsize=float(positionsiz)
                return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide)
            except:
                print('order failed', tick)
# order('BTCUSDT',0.001, 'BUY', 'SELL', 29000, 32000,28900, 'LONG',)
