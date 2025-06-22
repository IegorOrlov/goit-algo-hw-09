from greedy_algorithm import find_coins_greedy
from dynamic_algorithm import find_min_coins
import timeit

coins = [50, 25, 10, 6, 1]
amount = 113

print(f"Результат жадібного алгоритма: {find_coins_greedy(coins, amount)}")
print(f"Результат алгоритма динамічного програмування: {find_min_coins(coins, amount)}")

print("Змінюємо кінцеву суму:")
for amount in [113, 1133, 11333]:
    print(
        f"Час виконання жадібного алгоритма: {timeit.timeit(lambda:find_coins_greedy(coins, amount), number=100)}"
    )
    print(
        f"Час виконання динамічного програмування: {timeit.timeit(lambda:find_min_coins(coins, amount), number=100)}"
    )
print("Змінюємо набір монет:")
amount = 1133
for coins in [[50, 1], [50, 25, 10, 1], [50, 25, 10, 6, 5, 3, 2, 1]]:
    print(
        f"Час виконання жадібного алгоритма: {timeit.timeit(lambda:find_coins_greedy(coins, amount), number=100)}"
    )
    print(
        f"Час виконання динамічного програмування: {timeit.timeit(lambda:find_min_coins(coins, amount), number=100)}"
    )
