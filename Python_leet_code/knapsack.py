def knapsack(loot, weight_limit):
    grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
    for row, item in enumerate(loot):
        row = row + 1
        for col in range(weight_limit + 1):
            weight_capacity = col
            if item.weight <= weight_capacity:
                item_value = item.value
                item_weight = item.weight
                previous_best_less_item_weight = grid[row - 1][weight_capacity - item_weight]
                capacity_value_with_item = item_value + previous_best_less_item_weight
                capacity_value_without_item = grid[row - 1][col]
                grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
            else:
                grid[row][col] = grid[row - 1][col]

    return grid[-1][-1]