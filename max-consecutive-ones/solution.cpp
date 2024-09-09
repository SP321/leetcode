class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n=nums.size();
        int curr=0, mx=0;
        for(int i=0;i<n;i++){
            if(nums[i]==1){
                curr++;
            }
            else{
                mx=max(curr,mx);
                curr=0;
            }
        }
        return max(mx,curr);
    }
};