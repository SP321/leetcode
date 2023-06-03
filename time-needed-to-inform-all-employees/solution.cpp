class Solution {
public:
    vector<vector<int>> graph;
    vector<int> informTime;
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        this->graph = vector<vector<int>>(n);
        this->informTime = informTime;
        
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                this->graph[manager[i]].push_back(i);
            }
        }
        
        return dfs(headID);
    }
    
    int dfs(int node) {
        int ans = 0;
        for (int child : graph[node]) {
            ans = max(ans, dfs(child));
        }
        return ans + informTime[node];
    }
    
};