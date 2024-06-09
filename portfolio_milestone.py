class itemToPurchase:
    item_name = '0.00'
    item_price = 0.00
    item_quantity = 0

product1 = itemToPurchase()

product1.item_name = input('Enter name of product 1: ')
product1.item_price = float(input('Enter price of product 1: '))
product1.item_quantity = int(input('Enter quantity of product 1: '))

product2 = itemToPurchase()

product2.item_name = input('Enter name of product 2: ')
product2.item_price = float(input('Enter price of product 2: '))
product2.item_quantity = int(input('Enter quantity of product 2: '))

def print_item_cost(product):
    product_total = product.item_quantity * product.item_price
    return product_total

print('{} {} @ ${:.2f} = ${:.2f}'.format(product1.item_quantity, product1.item_name, product1.item_price, print_item_cost(product1)))
print('{} {} @ ${:.2f} = ${:.2f}'.format(product2.item_quantity, product2.item_name, product2.item_price, print_item_cost(product2)))
print('Grand total = ${:.2f}'.format((print_item_cost(product1) + print_item_cost(product2))))
