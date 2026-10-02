products = [ "Shoes", "Hat", "T-Shirts", "Pants"]
for product in products:
    print(product)

print('Using Enumerator')

for count, product in enumerate(products, start=1):
    print(count, product)


print('Getting input from user and adding it')
favourite_cricketers = []

while True:
    cricketer_name = input('Please enter your favourite cricketer: ')
    if(cricketer_name == "exit"):
        break;
    favourite_cricketers.append(cricketer_name)
print(favourite_cricketers)
