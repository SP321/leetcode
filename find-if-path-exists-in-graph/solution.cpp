class DSU {
public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
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

    bool unionSets(int x, int y) {
        int xr = find(x);
        int yr = find(y);
        if (xr == yr) {
            return false;
        }
        if (rank[xr] < rank[yr]) {
            std::swap(xr, yr);
        }
        parent[yr] = xr;
        if (rank[xr] == rank[yr]) {
            rank[xr]++;
        }
        return true;
    }

private:
    vector<int> parent;
    vector<int> rank;
};

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        DSU s(n);
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            s.unionSets(u, v);
        }
        return s.find(source) == s.find(destination);
    }
};