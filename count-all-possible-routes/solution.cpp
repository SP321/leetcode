class Solution {
public:
    int n;
    vector<vector<int>> dp;
    vector<int> x;
    int end;

    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        n = locations.size();
        x = locations;
        dp.resize(n, vector<int>(fuel + 1, -1));
        end=finish;
        return dfs(start, fuel);
    }

    int dfs(int i, int fuel) {
        if (dp[i][fuel] != -1) {
            return dp[i][fuel];
        }

        int ans = 0;
        if (i == end) {
            ans += 1;
        }

        for (int j = 0; j < n; j++) {
            if (j != i) {
                int fuelLeft = fuel - abs(x[j] - x[i]);
                if (fuelLeft >= 0) {
                    ans += dfs(j, fuelLeft);
                    ans %= 1000000007;
                }
            }
        }

        dp[i][fuel] = ans;
        return dp[i][fuel];
    }
};