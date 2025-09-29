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
client.delete("bag")
client.show()


# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон

class Phone:

    def __init__(self, number, battery_level=100):
        self.number = number
        self.battery_level = battery_level


    def used(self, percent):
        self.battery_level -= percent

        if  self.battery_level <= 20:
            print("Увага у вас залишилось меньше 20% заряду батареї")

        print(f"Залишилось {self.battery_level}% заряду батареї")


    def info(self):
        print(f"Номер телефону -- {self.number}"
              f"\nЗаряд телефону -- {self.battery_level}%")

telephone = Phone(32445234)

telephone.info()
telephone.used(20)
telephone.used(60)