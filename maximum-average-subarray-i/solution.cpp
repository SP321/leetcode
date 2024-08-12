class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double ans=-1e5;
        long long c=0;
        int i=0;
        for(int j=0;j<nums.size();j++){
            c+=nums[j];
            if(j-i+1>k){
                c-=nums[i];
                i+=1;
            }
            if(j-i+1==k){
                ans=max(ans,((double)c)/k);
            }
        }
        return ans;
    }
};