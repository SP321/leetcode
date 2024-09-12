class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        for i in range(3, len(arr)):
            if i >= 3 and arr[i] >= arr[i - 2] and arr[i - 1] <= arr[i - 3]:
                return True

            if i >= 4 and arr[i - 1] == arr[i - 3] and arr[i - 2] <= arr[i] + arr[i - 4]:
                return True

            if i >= 5 and arr[i - 2] >= arr[i - 4] and arr[i - 3] - arr[i - 5] <= arr[i - 1] <= arr[i - 3] and arr[i] >= arr[i - 2] - arr[i - 4]:
                return True
    
        return False