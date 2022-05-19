from core import session
def order_list():
    orders_ids = []
    all_ord = session.futures_get_open_orders()
    for ord in all_ord:

        orders_ids.append(ord['orderId'])
    return orders_ids


