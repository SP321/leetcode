template<typename T>
class Prefix2D {
private:
    vector<vector<T>> prefix;
public:
    Prefix2D() {}
    Prefix2D(vector<vector<T>> matrix) {
        int m = matrix.size(), n = matrix[0].size();
        prefix.resize(m + 1, vector<T>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1];
            }
        }
    }
    Prefix2D(const vector<string>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        prefix.resize(m + 1, vector<T>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+(matrix[i-1][j-1]=='A');
            }
        }
    }
    int getSum(int x1, int y1, int x2, int y2) {
        return prefix[x2 + 1][y2 + 1] - prefix[x2 + 1][y1] - prefix[x1][y2 + 1] + prefix[x1][y1];
    }
};

class Solution {
public:
    const int MOD = 1e9 + 7;

    int ways(std::vector<std::string>& pizza, int k) {
        int rows = pizza.size();
        int cols = pizza[0].size();

        Prefix2D<int> prefix(pizza);
        std::vector<std::vector<std::vector<uint64_t>>> dp(rows, std::vector<std::vector<uint64_t>>(cols, std::vector<uint64_t>(k, 0)));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j][0] = prefix.getSum(i, j, rows - 1, cols - 1) > 0;
            }
        }
        for (int s = 1; s < k; s++) {
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    uint64_t& cur = dp[i][j][s];
                    for (int r = i + 1; r < rows; r++) {
                        if (prefix.getSum(i, j, r - 1, cols - 1) > 0 && prefix.getSum(r, j, rows - 1, cols - 1) > 0) {
                            cur += dp[r][j][s - 1];
                            cur %= MOD;
                        }
                    }
                    for (int c = j + 1; c < cols; c++) {
                        if (prefix.getSum(i, j, rows - 1, c - 1) > 0 && prefix.getSum(i, c, rows - 1, cols - 1) > 0) {
                            cur += dp[i][c][s - 1];
                            cur %= MOD;
                        }
                    }
                }
            }
        }

        return dp[0][0][k - 1];
    }
};