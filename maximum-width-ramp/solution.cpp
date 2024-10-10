class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n=nums.size();
        vector<int>order(n);
        for(int i=0;i<n;i++)
            order[i]=i;
        sort(order.begin(),order.end(),[&nums](int i,int j){
            if (nums[i] == nums[j]) //stablesort
                return i < j;
            return nums[i] < nums[j];
        });
        int i=n;
        int ans=0;
        for(int& j:order){
            ans=max(ans,j-i);
            i=min(i,j);
        }
        return ans;
    }
};