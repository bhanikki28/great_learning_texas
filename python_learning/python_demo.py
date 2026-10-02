print('Learning List in Python');

product_names = ["T-Shirt", "Shoes", "Mart"]
print(product_names)
product_names.append('Shoes')
print('Proudct list got updated using append method')
print('Updated Product List', product_names)

print('Learing tuples in Python')
product_desc = ('Test')
print(product_desc)

print('Dictionary in Python')
product_prices = {
    "Shoes" : 49.0,
    "T-Shirts" : 30,
    "Mart" : 50
}

print("The price for Shoes ", product_prices.get("Shoes"))