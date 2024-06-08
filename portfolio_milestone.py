class ItemToPurchase:
    item_name = '0.00'
    item_price = 0.00
    item_quantity = 0

product1 = ItemToPurchase()

product1.item_name = input('Enter name of product 1: ')
product1.item_price = float(input('Enter price of product 1: '))
product1.item_quantity = int(input('Enter quantity of product 1: '))

product2 = ItemToPurchase()

product2.item_name = input('Enter name of product 2: ')
product2.item_price = float(input('Enter price of product 2: '))
product2.item_quantity = int(input('Enter quantity of product 2: '))

product1_total = product1.item_quantity * product1.item_price
product2_total = product2.item_quantity * product2.item_price
print('{} {} @ ${:.2f} = ${:.2f}'.format(product1.item_quantity, product1.item_name, product1.item_price, product1_total ))
print('{} {} @ ${:.2f} = ${:.2f}'.format(product2.item_quantity, product2.item_name, product2.item_price, product2_total ))
print('Grand total = ${:.2f}'.format(product1_total + product2_total))
