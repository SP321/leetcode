
class TreeAncestor {
public:
    int bin_max;
    vector<vector<int>> up;
    
    TreeAncestor(int n, vector<int>& parent) {
        bin_max = int(log2(n) + 1);
        
        up.resize(n, vector<int>(bin_max, -1));
        
        for (int i = 0; i < n; ++i) {
            up[i][0] = parent[i];
        }
        
        for (int j = 1; j < bin_max; ++j) {
            for (int i = 0; i < n; ++i) {
                if (up[i][j - 1] != -1) {
                    up[i][j] = up[up[i][j - 1]][j - 1];
                }
            }
        }
    }
    
    int getKthAncestor(int node, int k) {
        for (int j = 0; j < bin_max; ++j) {
            if (k & (1 << j)) {
                node = up[node][j];
                if (node == -1) return -1;
            }
        }
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */