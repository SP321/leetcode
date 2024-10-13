int MOD=int(1e9+7);
class Solution {
public:
    int countWinningSequences(string s) {
        string opts = "FWE";
        int n = s.size();
        
        auto score = [](char x, char y) -> int {
            if (x == y) return 0;
            if ((x == 'F' && y == 'E') || (x == 'W' && y == 'F') || (x == 'E' && y == 'W')) return 1;
            return -1;
        };

        vector<unordered_map<int, long long>> dp0(3);
        dp0[0][score(opts[0], s[0])] += 1;
        dp0[1][score(opts[1], s[0])] += 1;
        dp0[2][score(opts[2], s[0])] += 1;

        for (int i = 1; i < n; ++i) {
            vector<unordered_map<int, long long>> dp1(3);
            for (int move = 0; move < 3; ++move) {
                for (auto& [sc, v] : dp0[move]) {
                    for (int next_move = move + 1; next_move <= move + 2; ++next_move) {
                        int next = next_move % 3;
                        int new_score = sc + score(opts[next], s[i]);
                        dp1[next][new_score] += v;
                        dp1[next][new_score] %=MOD;

                    }
                }
            }
            dp0 = dp1;
        }

        int ans = 0;
        for (auto& c : dp0) {
            for (auto& [x, v] : c) {
                if (x > 0) {
                    ans += v;
                    ans%=MOD;
                }
            }
        }

        return ans;
    }
};