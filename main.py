# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).

class BankAccount:
    currencies = {"dollar": 1, "euro": 0.85, "pounds": 0.74, }

    def __init__(self, name, balance, currency="dollar"):
        if currency not in BankAccount.currencies:
            raise ValueError("Невідома валюта")

        else:
            self.name = name
            self.balance = balance
            self.currency = currency


    def info(self):
        print(f"Ім'я: {self.name}"
              f"\nБаланс: {self.balance}"
              f"\nВаш курс: {self.currency}"
              f"\nСпільний курс: {self.currencies}")


    def change_currency(self,new_currency):

        if new_currency in self.currencies:
            self.balance = (self.balance * BankAccount.currencies[self.currency]) / BankAccount.currencies[new_currency]
            self.currency = new_currency
        else:
            raise ValueError("Невідома валюта")


    def conversion(self, new_currency):

        new_balance = (self.balance * BankAccount.currencies[self.currency]) / BankAccount.currencies[new_currency]
        print(f"Конвертація - {new_balance} {new_currency}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError