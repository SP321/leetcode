class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        unordered_map<int, vector<int>> g;

        auto connect = [&](int n1, int n2) {
            g[n1].push_back(n2);
            g[n2].push_back(n1);
        };

        auto get_key = [&](int i, int j, char dir) {
            int d = (dir == 'l') ? 0 : (dir == 'r') ? 1 : (dir == 't') ? 2 : 3;
            return (i * n + j) * 4 + d;
        };

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j > 0) {
                    connect(get_key(i, j - 1, 'r'), get_key(i, j, 'l'));
                }
                if (i > 0) {
                    connect(get_key(i - 1, j, 'b'), get_key(i, j, 't'));
                }
                if (grid[i][j] == '\\') {
                    connect(get_key(i, j, 'l'), get_key(i, j, 'b'));
                    connect(get_key(i, j, 't'), get_key(i, j, 'r'));
                } else if (grid[i][j] == '/') {
                    connect(get_key(i, j, 'l'), get_key(i, j, 't'));
                    connect(get_key(i, j, 'b'), get_key(i, j, 'r'));
                } else {
                    connect(get_key(i, j, 'l'), get_key(i, j, 'b'));
                    connect(get_key(i, j, 't'), get_key(i, j, 'r'));
                    connect(get_key(i, j, 'l'), get_key(i, j, 't'));
                    connect(get_key(i, j, 'b'), get_key(i, j, 'r'));
                }
            }
        }

        unordered_set<int> visited;

        function<void(int)> dfs = [&](int x) {
            for (const auto& y : g[x]) {
                if (visited.find(y) == visited.end()) {
                    visited.insert(y);
                    dfs(y);
                }
            }
        };

        int ans = 0;
        for (const auto& x : g) {
            if (visited.find(x.first) == visited.end()) {
                dfs(x.first);
                cout<<x.first<<" "<<visited.size()<<endl;
                ++ans;
            }
        }

        return ans;
    }
};