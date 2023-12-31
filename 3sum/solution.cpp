class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>ans;
        for(int i=0;i<nums.size()-2;i++){
           if(i>0&&nums[i]==nums[i-1])continue;
           int l=i+1;
           int h=nums.size()-1;
           while(l<h){
                if(nums[i]+nums[l]+nums[h]==0){
                    ans.push_back({nums[i],nums[l],nums[h]});
                    l++;
                    while(nums[l]==nums[l-1]&&l<h)
                        l++;
                    h--;
                }else if(nums[i]+nums[l]+nums[h]>0){
                    h--;
                }else{
                    l++;
                }
           }
        }
        return ans;
    }
};