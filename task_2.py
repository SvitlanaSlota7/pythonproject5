def birthday_calculator():
    name = "Mary"
    current_age = 23
    current_year = 2026

    next_age = current_age + 1
    birth_year = current_year - current_age

    print(f"Hello {name}, on your next birthday you’ll be {next_age} years.")
    print(f"Apparently, you {name} were born in  {birth_year} !")


if __name__ == "__main__":
    birthday_calculator()
