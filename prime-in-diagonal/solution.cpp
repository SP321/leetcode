class Solution {
public:
    bool isprime(int x){
        if(x<2)
            return 0;
        for(int i=2;i*i<=x;i++)
            if(x%i==0)
                return 0;
        return 1;
    } 
    int diagonalPrime(vector<vector<int>>& nums) {
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(isprime(nums[i][i]))
                ans=max(ans,nums[i][i]);
            if(isprime(nums[i][nums.size() - i - 1]))
                ans=max(ans,nums[i][nums.size() - i - 1]);
        }
        return ans;
    }
};