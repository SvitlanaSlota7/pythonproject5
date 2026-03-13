import itertools


def all_combinations_hello():
    word = "hello"

    # всіх комбнації літер буде 120
    all_permutations = itertools.permutations(word)

    #  set для унікальних 60 комбінацій
    unique_results = set()
    for p in all_permutations:
        unique_results.add("".join(p))

    sorted_combinations = sorted(list(unique_results))

    print(f"Усі унікальні комбінації для слова '{word}' ({len(sorted_combinations)} варіантів):")
    print("-" * 50)

    # результат виводимо у вигляді 3 колонок

    for i, w in enumerate(sorted_combinations, 1):
        print(f"{i: >2}. {w}", end="\t")
        if i % 3 == 0:
            print()


if __name__ == "__main__":
    all_combinations_hello()
