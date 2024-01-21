class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x, y)
        ans = [0] * n
        for i in range(1, n + 1):
            ans[0] += 2 									# go left and right
            ans[min(i - 1, abs(i - y) + x)] -= 1 			# reach 1 then stop
            ans[min(n - i, abs(i - x) + 1 + n - y)] -= 1 	# reach n then stop
            ans[min(abs(i - x), abs(y - i) + 1)] += 1 	# reach x then split
            ans[min(abs(i - x) + 1, abs(y - i))] += 1 	# reach y then split
            r = max(x - i, 0) + max(i - y, 0)
            ans[r + (y - x + 0) // 2] -= 1 				# i -> x -> y <- x
            ans[r + (y - x + 1) // 2] -= 1 				# i -> y -> x <- y
        return list(accumulate(ans))