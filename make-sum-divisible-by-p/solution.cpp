class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n=nums.size();
        int diff=0;
        for(int i=0;i<n;i++){
            diff+=nums[i];
            diff%=p;
        }
        if(diff<0)
            diff+=p;
        if(!diff)
            return 0;
        unordered_map<int,int>d;
        d[0]=-1;
        int cur=0;
        int ans=n;
        for(int i=0;i<n;i++){
            cur+=nums[i];
            cur%=p;
            if(cur<0)
                cur+=p;
            int x=(cur-diff+p)%p;
            if(d.contains(x)){
                ans=min(ans,i-d[x]);
            }
            d[cur]=i;
        }
        return ans==n?-1:ans;                
    }
};