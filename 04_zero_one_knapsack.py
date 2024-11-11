def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    values = []
    weights = []
    
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        values.append(value)
        weights.append(weight)
    
    W = int(input("Enter the capacity of the knapsack: "))
    
    max_value, selected_items = knapsack_01(n, values, weights, W)
    
    print(f"Maximum value in knapsack: {max_value}")
    print("Selected items (indices):", selected_items)


"""Branch and Bound is an algorithmic technique used to solve optimization problems by exploring all possible solutions in 
a systematic way. In the context of sorting, it can be applied to problems where there are additional constraints, 
such as minimizing swaps or comparisons. The process involves branching into subproblems, bounding to evaluate the best 
possible solutions, and pruning to discard suboptimal paths. While not commonly used in traditional sorting algorithms, 
it can optimize constrained sorting tasks. It’s mainly used when sorting involves optimization beyond just arranging data in order.

Worst-case: O(2^n)
Best-case: O(n×W) 
This code implements the 0/1 Knapsack Problem using dynamic programming (DP). The goal is to maximize the value we can carry in a knapsack of limited capacity W without breaking any items, so each item is either fully taken or left out.

How It Works
DP Table Setup:

A 2D DP table dp is created where dp[i][w] represents the maximum value possible with the first i items and a knapsack capacity of w.
Filling the DP Table:

For each item (i) and each possible weight capacity (w):
If the item’s weight is less than or equal to the current capacity, 
we decide whether to include it by checking if adding its value gives a better result than excluding it.
Otherwise, we exclude the item.
Tracing the Selected Items:

After building the table, we backtrack through it to find the items included in the optimal solution by comparing values in the DP table.
Output:

The maximum value achievable (dp[n][W]) and the indices of the selected items.
Example of Usage
Enter the values and weights of items, then enter the knapsack’s capacity.
The code will output the maximum achievable value and a list of indices of items selected for the optimal solution.
Complexity
Time complexity: 
𝑂(𝑛×𝑊)
O(n×W), where 𝑛
n is the number of items.
Space complexity: 
𝑂(𝑛×𝑊)
O(n×W), due to the DP table size.
"""