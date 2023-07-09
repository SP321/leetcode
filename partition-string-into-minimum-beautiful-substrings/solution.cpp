class Solution {
public:
    set<string> power_of_5;
    vector<map<string, int>> dp;
    string s;
    int n;

    int minimumBeautifulSubstrings(string s) {
        long long pow5 = 1;
        for (int i = 0; i < 8; i++) {
            string binary = "";
            while (pow5) {
                binary = (pow5 & 1 ? '1' : '0') + binary;
                pow5 >>= 1;
            }
            power_of_5.insert(binary);
            pow5 = pow(5, i + 1);
        }
        this->s = s;
        n = s.size();
        dp.resize(n);

        int result = dfs(0, "");
        return result >= 20 ? -1 : result;
    }

    int dfs(int i, string prefix) {
        if (i == n) {
            if (prefix.empty()) {
                return 0;
            } else {
                return 69;
            }
        }

        if (dp[i][prefix] != 0) {
            return dp[i][prefix];
        }

        prefix += s[i];
        int ans = dfs(i + 1, prefix);
        if (power_of_5.count(prefix)) {
            ans = min(ans, 1 + dfs(i + 1, ""));
        }

        dp[i][prefix] = ans;
        return ans;
    }
};