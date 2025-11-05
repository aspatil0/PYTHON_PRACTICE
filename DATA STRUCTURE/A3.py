def fractional_knapsack(values, weights, capacity):
    ratio = [(v / w, v, w) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)
    total_value = 0
    for r, v, w in ratio:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += r * capacity
            break
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value in Knapsack =", max_value)
