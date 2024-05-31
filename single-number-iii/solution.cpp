class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long long xor_all=0;
        for(int &x: nums)
            xor_all^=x;
        int mask=(xor_all & xor_all-1)^xor_all;
        vector<int>ans(2);
        for(int &x: nums){
            if(x&mask){
                ans[0]^=x;
            }else{
                ans[1]^=x;
            }
        }
        return ans;
    }
};