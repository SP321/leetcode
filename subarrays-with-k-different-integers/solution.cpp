class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        int n=nums.size();
        auto helper=[&](int k){
            unordered_map<int,int>c;
            int ans=0;
            int i=0;
            int cc=0;
            for(int j=0;j<n;j++){
                if(c[nums[j]]==0)
                    cc+=1;
                c[nums[j]]+=1;
                while(cc>k){
                    c[nums[i]]-=1;
                    if(c[nums[i]]==0)
                        cc-=1;
                    i+=1;
                }
                ans+=j-i+1;
            }
            return ans;
        };
        return helper(k) - helper(k - 1);

    }
};