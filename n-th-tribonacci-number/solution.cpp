class Solution {
public:
    int tribonacci(int n) {
        unordered_map<int,int>memo;
        function<int(int)>dp=[&](int n){
            if(memo.find(n)!=memo.end())
                return memo[n];
            if(n==0)
                return 0;
            if(n<=2)
                return 1;
            return memo[n]=dp(n-1)+dp(n-2)+dp(n-3);
        };
        return dp(n);
    }
};