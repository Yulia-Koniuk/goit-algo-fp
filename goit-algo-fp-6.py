def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    result = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            result.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return result, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if item_list[i - 1][1]["cost"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_list[i - 1][1]["cost"]] + item_list[i - 1][1]["calories"])
            else:
                dp[i][j] = dp[i - 1][j]

    result = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(item_list[i - 1][0])
            j -= item_list[i - 1][1]["cost"]
        i -= 1

    total_cost = sum(items[item]["cost"] for item in result)
    total_calories = dp[n][budget]

    return result, total_cost, total_calories


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 100

# Використання жадібного алгоритму
print("Greedy Algorithm:")
items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Items:", items_greedy)
print("Total Cost:", total_cost_greedy)
print("Total Calories:", total_calories_greedy)

# Використання алгоритму динамічного програмування
print("\nDynamic Programming:")
items_dynamic, total_cost_dynamic, total_calories_dynamic = dynamic_programming(items, budget)
print("Items:", items_dynamic)
print("Total Cost:", total_cost_dynamic)
print("Total Calories:", total_calories_dynamic)


"""
Greedy Algorithm:
Items: ['cola', 'potato', 'pepsi', 'hot-dog']
Total Cost: 80
Total Calories: 870

Dynamic Programming:
Items: ['potato', 'cola', 'pepsi', 'pizza']
Total Cost: 100
Total Calories: 970
"""