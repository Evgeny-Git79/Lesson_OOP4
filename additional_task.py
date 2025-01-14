from email.policy import default

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
        print(f"Создан магазин {self.name}")

    def item_add(self, item_name, item_price):
        self.items.update({item_name : item_price})
        print (self.name, self.items)

    def item_remove(self, item_name):
        self.items.pop(item_name)
        print (self.items)

    def item_price_check(self, item_name):
        a = self.items.get(item_name, "none")
        print(a)

    def item_price_update(self, item_name, item_price):
        if self.items.get(item_name, "none") == "none":
            print("Такого товара нет")
        else:
            self.items.update({item_name: item_price})

        print(self.items)



name = "Имя1"
address = "Адрес1"
Store1 = Store(name, address)

name = "Имя2"
address = "Адрес2"
Store2 = Store(name, address)

name = "Имя3"
address = "Адрес3"
Store3 = Store(name, address)

item_name = "banan"
item_price = "10"

Store1.item_add(item_name, item_price)
Store2.item_add(item_name, item_price)
Store3.item_add(item_name, item_price)
Store1.item_remove(item_name)

item_name = "apple"
item_price = "20"
Store1.item_add(item_name, item_price)
Store1.item_price_check(item_name)
Store1.item_price_check("banan")

item_name = "apple"
item_price = "25"
Store1.item_price_update(item_name, item_price)







