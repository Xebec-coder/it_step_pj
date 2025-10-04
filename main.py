# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
import random
import json


def start_game():
    print("Комп'ютер загадав число від 1 до 100.")
    print("Спробуйте вгадати його! Якщо вгадаєте менш ніж за 5 спроб — ви перемогли!")

    attempts = 0
    num_comp = random.randint(1, 100)

    while True:
        try:
            num_user = int(input("Введіть число: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        if not 1 <= num_user <= 100:
            print("Число має бути від 1 до 100.")
            continue

        attempts += 1

        if num_user > num_comp:
            print("Потрібне число менше!")
        elif num_user < num_comp:
            print("Потрібне число більше!")
        else:
            print(f"Вітаю! Ви вгадали число {num_comp} за {attempts} спроб(и)!")
            if attempts < 5:
                print("✅ Ви перемогли!")
                return True
            else:
                print("❌ Комп’ютер переміг (більше ніж 4 спроби).")
                return False


def print_result(filename):              #Допрацюватим
    result = download_result(filename)
    wins = results["wins"]
    losses = results["losses"]
    print(f"Статистика ігор:")
    print(f"Перемог: {wins}")
    print(f"Програшів: {losses}")


def save_result(filename, results):              #Допрацюватим
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)


def download_result(filename):              #Допрацюватим
    try:
        with open(filename, "r", encoding="utf-8") as file:
            results = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        results = {"wins": 0, "losses": 0}
    return results


def main():
    filename = "results.json"
    results = download_result(filename)

    while True:
        print_result(filename)
        choice = input("\nХочете початии нову гру? (y/n): ").strip().lower()

        if choice == "y":
            user_won = start_game()
            if user_won:
                results["wins"] += 1
            else:
                results["losses"] += 1
            save_result(filename, results)
        elif choice == "n":
            print("Дякуємо за гру! До побачення!")
            break
        else:
            print("Введіть лише 'y' або 'n'.")


if __name__ == "__main__":
    main()