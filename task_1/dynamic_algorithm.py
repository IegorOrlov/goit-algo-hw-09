def find_min_coins(coins: list[int], amount: int) -> dict[int, int]:
    # Ініціалізація списку dp для зберігання мінімальної кількості монет для кожної суми
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # 0 монет потрібно, щоб зібрати 0

    # Словник, що зберігає останню використану монету для кожної суми
    last_coin = [0] * (amount + 1)

    # Динамічне заповнення dp
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення відповіді
    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result
