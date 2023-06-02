class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector<vector<int>> graph(n);
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n; ++j) {
                int x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
                int x2 = bombs[j][0], y2 = bombs[j][1], r2 = bombs[j][2];
                double dist = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
                if(dist <= r1) graph[i].push_back(j);
                if(dist <= r2) graph[j].push_back(i);
            }
        }
        vector<bool> visited(n, false);
        int ans = 0;
        for(int i = 0; i < n; ++i) {
            fill(visited.begin(), visited.end(), false);
            ans = max(ans, dfs(i, graph, visited));
        }
        return ans;
    }
private:
    int dfs(int i, vector<vector<int>>& graph, vector<bool>& visited) {
        visited[i] = true;
        int size = 1;
        for(auto j : graph[i]) {
            if(!visited[j]) size += dfs(j, graph, visited);
        }
        return size;
    }
};