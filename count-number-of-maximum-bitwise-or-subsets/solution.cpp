class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n=nums.size();
        vector<int>c(1<<17);
        int ans=0;
        for(int mask=0; mask< 1<<n; mask++){
            int cur=0;
            for(int i=0; i<n; i++){
                if( mask>>i&1 )
                    cur|=nums[i];
            }
            c[cur]+=1;
            if( c[cur]>ans )
                ans=c[cur];
        }
        return ans;
    }
};