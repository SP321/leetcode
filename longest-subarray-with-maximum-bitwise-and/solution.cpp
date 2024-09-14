class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int mx=*max_element(nums.begin(),nums.end());
        int c=0,ans=0;
        for(int &x:nums){
            if(x==mx){
                c+=1;
                ans=max(ans,c);
            }else{
                c=0;
            }
        }
        return ans;
    }
};