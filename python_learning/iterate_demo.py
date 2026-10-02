products = [ "Shoes", "Hat", "T-Shirts", "Pants"]
for product in products:
    print(product)

print('Using Enumerator')

for count, product in enumerate(products, start=1):
    print(count, product)