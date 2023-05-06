class Solution {
int powerMod(long long a, long long b, int m)
{
    long long res = 1;
    a = a % m;
    while(b>0)
    {
        if(b&1)
            res = (res * a) % m;
        a = a * a;
        a%=m;
        b = b >> 1;
    }
    return res;
}

public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int i=0;
        int j=n-1;
        int ans=0;
        int md=1e9+7;
        while(1){
            while (i<=j && nums[i]+nums[j] >target)
                j--;
            if(i>j || nums[i]+nums[j] >target)
                break;
            ans+=powerMod(2,j-i,md);
            ans%=md;
            i++;
        }
        return ans;
    }
};