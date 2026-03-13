import random


def guess_the_number_loop():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Я загадала число від 1 до 10. Спробуй його знайти!")

    # Використовуємо цикл True
    while True:
        try:
            user_guess = int(input("\nТвій варіант відповіді: "))
            attempts += 1

            if user_guess == secret_number:
                print(f" Вітаю! Ти вгадав за {attempts} спроб(и).")
                break  # цикл перерваний

            if user_guess < secret_number:
                print("Моє число більше.")
            else:
                print("Моє число менше.")

        except ValueError:
            print("Введи коректне ціле число.")


if __name__ == "__main__":
    guess_the_number_loop()
