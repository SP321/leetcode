class Solution {
public:
    int n;
    vector<vector<int>>adj;
    vector<bool>seen;
    int d;
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        this->n=n;
        d=destination;
        adj.resize(n,vector<int>(0));
        seen.resize(n);
        for(auto &edge: edges){
            int u=edge[0];
            int v=edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        return dfs(source);
    }
    bool dfs(int i){
        if(i==d)
            return 1;
        bool ans=0;
        seen[i]=1;
        for(auto &x:adj[i])
            if(!seen[x])
                ans=ans || dfs(x);
        return ans;
    }
};