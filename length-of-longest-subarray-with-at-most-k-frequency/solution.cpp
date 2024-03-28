class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int,int>c;
        int i=0,ans=0;
        for(int j=0;j<nums.size();j++){
            c[nums[j]]+=1;
            while(c[nums[j]]>k){
                c[nums[i]]-=1;
                i+=1;
            }
            ans=max(ans,j-i+1);
        }
        return ans;
    }
};