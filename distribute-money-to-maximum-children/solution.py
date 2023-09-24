class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1

        c = money // 7
        remaining = money % 7

        if c == children and remaining == 0:
            return children

        if c == children - 1 and remaining == 3:
            return children - 2

        return min(children - 1, c)