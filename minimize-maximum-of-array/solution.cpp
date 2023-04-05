class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        int i=0;
        int j=1e9+1;
        long long ans=1e9+1;
        while(i<=j){
            int mid=(i+j)/2;
            long long move=0;
            for(int k=nums.size()-1;k>=0;k--){
                long long temp=nums[k]+move;
                move=0;
                if(temp>mid)
                    move=temp-mid;
            }
            if(move==0){
                ans=min(ans,(long long) mid);
                j=mid-1;
            }
            else
                i=mid+1;
        }
        return ans;
    }
};