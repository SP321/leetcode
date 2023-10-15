class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_left_index = [-1] * n
        max_left_index = [-1] * n
        min_right_index = [-1] * n
        max_right_index = [-1] * n

        min_left_index[0] = 0
        max_left_index[0] = 0
        min_right_index[n - 1] = n - 1
        max_right_index[n - 1] = n - 1

        for i in range(1, n):
            if nums[i] < nums[min_left_index[i - 1]]:
                min_left_index[i] = i
            else:
                min_left_index[i] = min_left_index[i - 1]

            if nums[i] > nums[max_left_index[i - 1]]:
                max_left_index[i] = i
            else:
                max_left_index[i] = max_left_index[i - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[min_right_index[i + 1]]:
                min_right_index[i] = i
            else:
                min_right_index[i] = min_right_index[i + 1]

            if nums[i] > nums[max_right_index[i + 1]]:
                max_right_index[i] = i
            else:
                max_right_index[i] = max_right_index[i + 1]

        for i in range(n):
            j = i + indexDifference
            if j < n:
                if nums[max_right_index[j]] - nums[min_left_index[i]] >= valueDifference:
                    return [min_left_index[i], max_right_index[j]]
                if nums[max_left_index[i]] - nums[min_right_index[j]] >= valueDifference:
                    return [max_left_index[i], min_right_index[j]]

        return [-1, -1]