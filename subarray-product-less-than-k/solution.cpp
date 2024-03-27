class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n=nums.size();
        long long p=1;
        int ans=0;
        int i=0;
        for(int j=0;j<n;j++){
            p*=nums[j];
            while (i<j and p>=k){
                p/=nums[i];
                i+=1;
            }
            if(p<k)
                ans+=j-i+1;
        }
        return ans;
    }
};