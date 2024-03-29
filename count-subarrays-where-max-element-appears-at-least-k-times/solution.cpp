class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int mx=*max_element(nums.begin(),nums.end());
        int n=nums.size(),i=0;
        long long ans=0;
        unordered_map<int,int>c;
        for(int j=0;j<n;j++){
            c[nums[j]]+=1;
            while (c[mx]>=k){
                c[nums[i]]-=1;
                i+=1;
            }
            ans+=i;
        }
        return ans;
    }
};