class Solution {
public:
    int waysToReachStair(int k) {
        map<pair<int, int>, int> memo;

        function<int(int, int)> dp = [&](int pos, int jump) -> int {
            if (pos > k + 1) {
                return 0;
            }
            auto key = make_pair(pos, jump);
            if (memo.count(key)) {
                return memo[key];
            }
            int ans = int(pos == k)+ int(pos - 1 == k);
            ans += dp(pos - 1 + (1 << jump), jump + 1);
            ans += dp(pos + (1 << jump), jump + 1);
            return memo[key] = ans;
        };
        return dp(1, 0);
    }
};