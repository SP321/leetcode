class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(!size(edges)) return {0};
        vector<vector<int>> g(n);
        for(auto& e : edges) 
            g[e[0]].push_back(e[1]), 
            g[e[1]].push_back(e[0]);
        vector<int> leaves, newLeaves, inDegree;
        for(int i = 0; i < n; i++) {
            if(size(g[i]) == 1)
                leaves.push_back(i);
            inDegree.push_back(size(g[i]));
        }
        while(n > 2) {
            for(auto leaf : leaves) 
                for(auto adj : g[leaf])
                    if(--inDegree[adj] == 1)
                        newLeaves.push_back(adj);
            n -= size(leaves);
            leaves = move(newLeaves);
        }
        return leaves;
    }
};