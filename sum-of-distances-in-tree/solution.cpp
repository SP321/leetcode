class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        unordered_map<int,vector<int>>g;
        vector<int>ans(n);
        vector<int>c(n,1);
        for(auto &p:edges){
            int u=p[0],v=p[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        function <void(int,int)> dfs=[&](int u, int p){
            for(int &v:g[u]){
                if(v != p){
                    dfs(v, u);
                    c[u] += c[v];
                    ans[u] += ans[v] + c[v];
                }
            }
        };
        function <void(int,int)> dfs2=[&](int u, int p){
            for(int &v:g[u]){
                if(v != p){
                    ans[v] = ans[u] - c[v] + n - c[v];
                    dfs2(v, u);
                }
            }
        };
        dfs(0, -1);
        dfs2(0, -1);
        return ans;
    }
};