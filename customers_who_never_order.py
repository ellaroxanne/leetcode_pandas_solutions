import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # select customers where their id isn't in "orders"
    no_order_customers = customers[~customers['id'].isin(orders['customerId'])]
    names = no_order_customers[['name']].rename(columns = {'name': 'Customers'})
    return names
