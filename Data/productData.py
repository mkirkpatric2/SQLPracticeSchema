import random

products = []
for x in range(25):
    products.append("product" + f"{x+1}")

prices = []
for x in range(25):
    price = (random.randint(1, 15)*1000)+999
    prices.append(price)
