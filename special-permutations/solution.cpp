using namespace std;

class Solution {
public:
    const int MOD = 1e9 + 7;
    int n;
    vector<unordered_set<int>> graph;
    vector<vector<int>> dp;

    int specialPerm(vector<int>& nums) {
        n = nums.size();
        graph.resize(n);
        dp.resize(1 << n, vector<int>(n, -1));

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0) {
                    graph[i].insert(j);
                    graph[j].insert(i);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += dfs(1 << i, i);
            ans %= MOD;
        }
        return ans;
    }

    int dfs(int mask, int i) {
        if (dp[mask][i] != -1) {
            return dp[mask][i];
        }
        if (mask == (1 << n) - 1) {
            return 1;
        }
        int count = 0;
        for (int j : graph[i]) {
            if (!((mask >> j) & 1)) {
                count += dfs(mask | (1 << j), j);
                count %= MOD;
            }
        }
        dp[mask][i] = count;
        return count;
    }
};