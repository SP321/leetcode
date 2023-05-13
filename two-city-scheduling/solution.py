class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])

        total_cost = 0
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]

        return total_cost