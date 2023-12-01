class myList:
    def __init__(self, x):
        self.x = x
        self.popleft_c = 0

    def __getitem__(self, index):
        if index < self.popleft_c:
            return -inf
        return self.x[index]

    def __len__(self):
        return len(self.x)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        pos=0
        arr=myList(nums)
        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                arr.popleft_c=i
                x=bisect_right(arr,arr[i])
                nums[pos]=nums[i]
                i=x
            else:
                nums[pos]=nums[i]
                i+=1
            pos+=1
        return pos
