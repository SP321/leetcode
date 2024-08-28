class Solution {
public:
    string largestPalindrome(int n, int k) {
        vector<vector<bool>> dp((n + 1) / 2 + 1, vector<bool>(k, false));
        vector<vector<int>> prev((n + 1) / 2 + 1, vector<int>(k, -1));
        dp[(n + 1) / 2][0] = true;

        vector<int> p(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            p[i] = (p[i - 1] * 10) % k;
        }

        for (int i = (n + 1) / 2 - 1; i >= 0; --i) {
            for (int r = 0; r < k; ++r) {
                if (!dp[i + 1][r]) continue;
                for (int d = 9; d >= 0; --d) {
                    int coeff = p[i];
                    if (i != n - i - 1) {
                        coeff = (coeff + p[n - i - 1]) % k;
                    }
                    int nr = (r - d * coeff) % k;
                    if (nr < 0) nr += k;
                    dp[i][nr] = true;
                    prev[i][nr] = r;
                }
            }
        }

        string ans(n, '0');
        int curr_r = 0;
        for (int i = 0; i < (n + 1) / 2; ++i) {
            bool found = false;
            for (int d = 9; d >= 0; --d) {
                int coeff = p[i];
                if (i != n - i - 1) {
                    coeff = (coeff + p[n - i - 1]) % k;
                }
                int nr = (curr_r + d * coeff) % k;
                if (dp[i + 1][nr]) {
                    ans[i] = ans[n - i - 1] = '0' + d;
                    curr_r = nr;
                    found = true;
                    break;
                }
            }
            if (!found) return "0";
        }
        return ans;
    }
};