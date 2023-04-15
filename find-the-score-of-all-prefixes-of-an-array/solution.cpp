class Solution {
public:
    vector<long long> findPrefixScore(vector<int>& nums) {
        vector<long long>ans;
        vector<long long>ma;
        for(int i=0;i<nums.size();i++){
            ma.push_back(nums[i]);
            ans.push_back(nums[i]);
        }
        ans[0]*=2;
        for(int i=1;i<nums.size();i++){
            ma[i]=max(ma[i],ma[i-1]); 
            ans[i]=nums[i]+ma[i];
       }
        
        for(int i=1;i<nums.size();i++)
            ans[i]=ans[i]+ans[i-1];

        return ans;
    }
};