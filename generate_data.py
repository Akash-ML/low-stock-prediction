import random
import pandas as pd

data = []

for _ in range(2000):
    quantity = random.randint(0, 100)
    avg_daily_sales = random.randint(1, 20)
    days_to_restock = random.choice([3, 5, 7])
    price = random.randint(1, 500) * random.choice([1, 10, 100])

    low_stock = int(quantity < avg_daily_sales * days_to_restock)

    data.append([
        quantity,
        avg_daily_sales,
        days_to_restock,
        price,
        low_stock
    ])

df = pd.DataFrame(data, columns=[
    "quantity",
    "avg_daily_sales",
    "days_to_restock",
    "price",
    "low_stock"
])

df.to_csv("low_stock_data.csv", index=False)