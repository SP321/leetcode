class DSU {
public:
    vector<int> parent, rank;

    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    int unionSet(int x, int y) {
        int xr = find(x);
        int yr = find(y);
        if (xr == yr) {
            return xr;
        }
        if (rank[xr] < rank[yr]) {
            swap(xr, yr);
        }
        parent[yr] = xr;
        if (rank[xr] == rank[yr]) {
            ++rank[xr];
        }
        return xr;
    }
};
class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DSU dsu(n);
        vector<int>a(n,(1<<30)-1);
        for (auto& edge : edges) {
            int x=dsu.find(edge[0]);
            int y=dsu.find(edge[1]);
            a[dsu.unionSet(edge[0], edge[1])]=a[x]&edge[2]&a[y];
        }

        vector<int> ans;
        for (auto& q : query) {
            if (q[0] == q[1]) {
                ans.push_back(0);
                continue;
            }
            int x = dsu.find(q[0]);
            int y = dsu.find(q[1]);
            if (x != y) {
                ans.push_back(-1);
            } else {
                ans.push_back(a[x]);
            }
        }
        return ans;
    }
};
