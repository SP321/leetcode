class Solution {
public:
    struct hash_pair {
            template <class T1, class T2>
            size_t operator () (const pair<T1, T2>& p) const {
                auto hash1 = hash<T1>{}(p.first);
                auto hash2 = hash<T2>{}(p.second);
                return hash1 ^ hash2;
            }
    };
    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size(), m = board[0].size();
        unordered_map<char, int> word_counts;
        for (char c : word) word_counts[c]++;

        
        unordered_map<char, unordered_set<pair<int, int>, hash_pair>> word_pos;
        for (int x = 0; x < n; ++x) {
            for (int y = 0; y < m; ++y) {
                char ch = board[x][y];
                if (word_counts.find(ch) != word_counts.end()) {
                    word_pos[ch].insert({x, y});
                }
            }
        }

        for (auto& wc : word_counts) {
            if (word_pos[wc.first].size() < wc.second) return false;
        }

        if (word_counts[word[0]] > word_counts[word.back()]) {
            reverse(word.begin(), word.end());
        }

        function<bool(int, int, int)> dp = [&](int x, int y, int i) -> bool {
            if (x < 0 || x >= n || y < 0 || y >= m) return false;
            if (board[x][y] != word[i]) return false;
            if (i + 1 >= word.length()) return true;

            char temp = board[x][y];
            board[x][y] = '#';
            bool ans = dp(x + 1, y, i + 1) ||
                       dp(x - 1, y, i + 1) ||
                       dp(x, y + 1, i + 1) ||
                       dp(x, y - 1, i + 1);
            board[x][y] = temp;
            return ans;
        };

        for (auto& pos : word_pos[word[0]]) {
            if (dp(pos.first, pos.second, 0)) return true;
        }

        return false;
    }
};