from core import session
from positioncheck import order_list
from tickers import list_of_tickers
from order import order
import time

#  parameters to pass
size_USDT = 10




# def leverage_change(leveragex):
#     print("CHANGING LEVERAGE...")
#     for tick in list_of_tickers:
#         session.futures_change_leverage(symbol=tick, leverage=leveragex)
#         try:
#             session.futures_change_margin_type(symbol=tick, marginType='CROSSED')
#         except:
#             pass
#     print("LEVERAGE CHANGED SUCCESSFULLY")

# leverage_change(40)
current_orders = []

# async def check_orphan_orders():
#     while True:
#         orders = order_list()
#         for current in current_orders:
#             if current[0] in orders and current[1] in orders:
#                 pass
#             else:
#                 try:
#                     await session.futures_cancel_order(symbol=tick, orderId=current[1])
#                 except:
#                     pass
#                 try:
#                     await session.futures_cancel_order(symbol=tick, orderId=current[0])
#                 except:
#                     pass

while True:
    for tick in list_of_tickers:
        klines = session.futures_historical_klines(tick, '15m', '30 min ago')
        candle = klines[0]
        candle_open = float(candle[1])
        entry = float(candle[4])
        candle_high = float(candle[2])
        candle_low = float(candle[3])
        if candle_open>=entry:
            sidee='SELL'
            diee='BUY'
            pSide='SHORT'
            sll = candle_high
            tpp = entry - (candle_high - entry)
        else:
            sidee='BUY'
            diee='SELL'
            pSide='LONG'
            sll = candle_low
            tpp = entry + (entry - candle_low)
        positionsize=  size_USDT / entry
        current_orders.append(order(tick=tick, positionsize=positionsize, side = sidee, diee=diee, entry=entry, tp=tpp, sl=sll, pSide = pSide))
    for i in range(1,60):
        time.sleep(15)
        orders = order_list()
        print(order_list)
        print(current_orders)
        for current in current_orders:
            try:
                if (current[0] not in orders) or (current[1] not in orders):
                    for tick in list_of_tickers:
                        try:
                            session.futures_cancel_order(tick, current[0])
                        except:
                            pass
                        try:
                            session.futures_cancel_order(tick, current[1])
                        except: 
                            pass
                        try:
                            session.futures_cancel_order(tick, current[2])
                        except: 
                            pass                  
            except:
                print('exception here')
    # time.sleep(899)

# session.futures_create_order(
#     symbol='BTCUSDT',
#     quantity=0.01,
#     type='LIMIT',
#     side='BUY',
#     timeInForce= 'GTC',
#     price=1000
#     )