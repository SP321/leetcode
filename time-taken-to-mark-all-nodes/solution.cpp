class Solution {
public:
    vector<int> timeTaken(vector<vector<int>>& edges) {
        unordered_map<int, vector<pair<int, int>>> g;
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            g[u].push_back({v, (v & 1) ? 1 : 2});
            g[v].push_back({u, (u & 1) ? 1 : 2});
        }

        int n = g.size();
        vector<int> leaf_dist(n, 0), dist(n, 0);

        function<void(int, int)> dfs = [&](int u, int p) {
            leaf_dist[u] = 0;
            for (auto& [v, w] : g[u]) {
                if (v == p) continue;
                dfs(v, u);
                leaf_dist[u] = max(leaf_dist[u], leaf_dist[v] + w);
            }
        };

        function<void(int, int)> dfs2 = [&](int u, int p) {
            int mx = 0, smx = 0;
            for (auto& [v, w] : g[u]) {
                if (v == p) continue;
                int cur = leaf_dist[v] + w;
                if (cur > mx) {
                    smx = mx;
                    mx = cur;
                } else if (cur > smx) {
                    smx = cur;
                }
            }

            int up = (u & 1) ? 1 : 2;
            for (auto& [v, w] : g[u]) {
                if (v == p) continue;
                if (leaf_dist[v] + w == mx) {
                    dist[v] = max(dist[v], max(dist[u], smx) + up);
                } else {
                    dist[v] = max(dist[v], max(dist[u], mx) + up);
                }
                dfs2(v, u);
            }
        };

        dfs(0, -1);
        dfs2(0, -1);
        for (int i = 0; i < n; ++i) {
            dist[i] = max(dist[i], leaf_dist[i]);
        }
        return dist;
    }
};