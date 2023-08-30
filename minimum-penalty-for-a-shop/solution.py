class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_y = 0
        total_n = 0

        for i in customers:
            if i == 'Y':
                total_y += 1
            else:
                total_n += 1

        ans = 0
        minp = total_y
        current_n = 0
        current_y = 0

        for i in range(len(customers)):
            if customers[i] == 'N':
                current_n += 1
            else:
                current_y += 1

            p = current_n + (total_y - current_y)

            if p < minp:
                minp = p
                ans = i + 1

        return ans