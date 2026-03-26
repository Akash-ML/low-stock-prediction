import random
import pandas as pd

data = []

def generate_price():
    price = random.random()

    # Chances - Low tier 35%, Mid tier 35%, High tier 30%
    if price < 0.35:
        return round(random.uniform(1, 100), 2)
    elif price < 0.70:
        return round(random.uniform(100, 1000), 2)
    else:
        return round(random.uniform(1000, 5000), 2)

for _ in range(5000):
    quantity = random.randint(0, 100)
    days_to_restock = random.choice([3, 5, 7])
    price = generate_price()

    if random.random() < 0.3:  # 30% chance of value bet. 0 and 1
        avg_daily_sales = round(random.uniform(0, 1), 2)
    else:
        avg_daily_sales = round(random.uniform(1, 20), 2)

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