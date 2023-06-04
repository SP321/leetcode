class Solution {
public:
    vector<vector<int>>adj;
    int n;
    vector<bool>visited;
    void dfs(int i) {
        visited[i] = true;
        for (int j=0; j<n; j++) {
            if (adj[i][j]==1 && visited[j]==false) {
                dfs(j);
            }
        }
    }
    
    int findCircleNum(vector<vector<int>>& k) {
        n = k.size();
        adj=k;
        visited.resize(n, false);
        int ans = 0;
        for (int i=0; i<n; i++) {
            if (visited[i]==false) {
                ans++;
                dfs(i);
            }            
        }
        return ans;
    }
};