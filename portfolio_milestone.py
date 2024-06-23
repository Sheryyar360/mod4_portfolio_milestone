class ItemToPurchase:

    def __init__(self):
        self.item_name = ''
        self.item_price = 0.00
        self.item_quantity = 0

    def item_total(self):
        item_total = self.item_quantity * self.item_price
        return item_total


product1 = ItemToPurchase()
product1.item_name = input('Enter name of product 1: ')
product1.item_price = float(input('Enter price of product 1: '))
product1.item_quantity = int(input('Enter quantity of product 1: '))

product2 = ItemToPurchase()
product2.item_name = input('Enter name of product 2: ')
product2.item_price = float(input('Enter price of product 2: '))
product2.item_quantity = int(input('Enter quantity of product 2: '))


print('{} {} @ ${:.2f} = ${:.2f}'.format(product1.item_quantity, product1.item_name, product1.item_price,
                                         product1.item_total()))
print('{} {} @ ${:.2f} = ${:.2f}'.format(product2.item_quantity, product2.item_name, product2.item_price,
                                         product2.item_total()))
print('Grand total = ${:.2f}'.format((product1.item_total(), product2.item_total())))
