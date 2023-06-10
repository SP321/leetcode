class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans,quad=[],[]
        def ksum(k,start,target):
            print(k,quad)
            if k==2:
                l,r=start,len(nums)-1
                while l<r:
                    if nums[l]+nums[r]<target:
                        l+=1
                    elif nums[l]+nums[r]>target:
                        r-=1
                    else:
                        ans.append(quad+[nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
            else:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])
                    quad.pop()
            
        ksum(4,0,target)
        return ans
                    