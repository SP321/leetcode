class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        nums+=[float('inf')]
        presum=[0]+list(accumulate(nums))
        best_left_index=defaultdict(int)# assume best subarray to merge left is [0,i)
        dp=defaultdict(int) # dp[i]= count no of subarrays to left of i.
        
        for i in range(1,n+1):
            #choose smallest current subarray.(maximize left index.)
            best_left_index[i]=max(best_left_index[i-1],best_left_index[i]) 

            # 1 is current subarray + dp[best_left_index[i]] is count subarrays to left.
            dp[i]= 1 + dp[best_left_index[i]] 

            # If we are merging [left_index,i) , let next segment is [i,right_index).
            # choose smallest possible right_index. such that range_sum( [left_index,i) ) <= range_sum( [i,right_index) ).
            # presum[i]-presum[left_index]<=presum[right_index]-presum[i].
            # 2*presum[i]-presum[left_index]<=presum[right_index]
            # binary search for smallest possible right index.
            right_index=bisect.bisect_left(presum,2*presum[i]-presum[best_left_index[i]])
    
            best_left_index[right_index]=i

        return dp[n]
