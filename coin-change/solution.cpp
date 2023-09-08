class Solution {
public:
    vector<int> coins;
    int big;
    vector<vector<int>> dp;

    int coinChange(vector<int>& coins, int amount) {
        this->coins = coins;
        this->big = amount + 1;
        dp.resize(coins.size(), vector<int>(amount + 1, 0));
        
        int result = dfs(0, amount);
        
        return result >= big ? -1 : result;
    }

    int dfs(int i, int target) {
        if (target == 0) {
            return 0;
        }

        if (i == coins.size() || target < 0) {
            return big;
        }

        if (dp[i][target] != 0) {
            return dp[i][target];
        }

        dp[i][target] = min(
            dfs(i, target - coins[i]) + 1,
            dfs(i + 1, target)
        );
        
        return dp[i][target];
    }
};