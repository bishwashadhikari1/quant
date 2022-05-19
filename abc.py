from core import session

a = session.futures_get_open_orders()

for b in a:
    print(b)