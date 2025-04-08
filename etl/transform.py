import pandas as pd

customers = pd.read_csv("customer_project/data/processed_customers.csv")
orders = pd.read_csv("customer_project/data/processed_orders.csv")
products = pd.read_csv("customer_project/data/processed_products.csv")


orders["order_date"] = pd.to_datetime(orders["order_date"])


product_prices = products.set_index("product_id")["price"].to_dict()
orders["price"] = orders["product_id"].map(product_prices)
orders["order_amount"] = orders["quantity"] * orders["price"]


merged = orders.merge(customers, on="customer_id").merge(products, on="product_id")


merged.to_csv("customer_project/data/final_dataset.csv", index=False)


