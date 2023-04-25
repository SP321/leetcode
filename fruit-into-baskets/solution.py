class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        fruit_count = {}
        left = right = 0
        max_fruits = 0

        while right < n:
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits