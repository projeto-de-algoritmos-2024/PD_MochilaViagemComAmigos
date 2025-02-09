from typing import List, Tuple

def knapsack_multi(items: List[Tuple[str, int, int]], capacities: List[int]) -> Tuple[int, List[List[object]]]:
    n = len(items)
    k = len(capacities)
    dp = [[[0] * (cap + 1) for _ in range(n + 1)] for cap in capacities]
    
    # Fill DP table
    for i in range(1, n + 1):
        name, value, weight = items[i - 1]
        for j in range(k):
            for w in range(capacities[j], -1, -1):
                if weight <= w:
                    dp[j][i][w] = max(dp[j][i - 1][w], value + dp[j][i - 1][w - weight])
                else:
                    dp[j][i][w] = dp[j][i - 1][w]
    
    # Backtrack to find selected items for each backpack
    selected = [[] for _ in range(k)]
    used_items = set()
    for j in range(k):
        w = capacities[j]
        for i in range(n, 0, -1):
            if i - 1 not in used_items and dp[j][i][w] != dp[j][i - 1][w]:
                name, value, weight = items[i - 1]
                if w >= weight and dp[j][i][w] == value + dp[j][i - 1][w - weight]:
                    selected[j].append({"NomeItem": name, "Valor": value, "Peso": weight})
                    w -= weight
                    used_items.add(i - 1)
    
    for lst in selected:
        lst.reverse()

    valorTotal = 0
    for mochila in selected:
        for item in mochila:
            valorTotal += item["Valor"]
    return valorTotal, selected
