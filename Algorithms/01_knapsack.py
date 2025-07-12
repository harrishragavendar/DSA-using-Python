def knapsack(weights, values, capacity):
    item_count = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    values[i - 1] + dp[i - 1][j - weights[i - 1]],  # include the item
                    dp[i - 1][j]  # exclude the item
                )
            else:
                dp[i][j] = dp[i - 1][j]
    return dp


if __name__ == '__main__':
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    solution = knapsack(weights, values, capacity)
    for row in solution:
        print(row)
