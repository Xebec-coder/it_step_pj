# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:

    def __init__(self, name, items):
        self.name = name
        if items:
            self.items = items
        else:
            self.items = []


    def add(self, item):
        self.items.append(item)


    def delete(self, item):
        self.items.remove(item)


    def show(self):
        print(self.items)

my_bag = ["shield", "bag"]
client = Cart('John', my_bag)

client.add("bag")
client.add("key")
client.add("sword")
# client.delete("bag")
client.show()