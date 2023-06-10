class Solution:
	def maxValue(self, n: int, index: int, maxSum: int) -> int:
		maxSum = maxSum - n
		def solve(value):
			lm = max(0, value - index)
			ans = (value + lm) * (value - lm + 1) // 2
			lm = max(0, value - ((n-1) - index))
			ans = ans + (value + lm ) * (value - lm + 1) // 2
			return (ans - value)
		l , r = 0, maxSum
		while l < r:
			m = (l + r + 1) // 2
			if solve(m) <= maxSum:
				l = m
			else:
				r = m - 1
		return l + 1