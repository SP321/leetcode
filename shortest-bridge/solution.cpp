class Solution {
public:
    vector<pair<int, int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    vector<vector<int>> a;
    queue<pair<int, int>> bfs;
    int n;

    void dfs(int i, int j) {
        if (i < 0 || j < 0 || i >= n || j >= n ||a[i][j] != 1)
            return;
        a[i][j] = 2;
        bfs.push({i, j});
        for(auto dir : directions)
            dfs(i + dir.first, j + dir.second);
    }
    
    void findFirstIsland() {
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++) 
                if(a[i][j] == 1) {
                    dfs(i, j);
                    return;
                }
    }

    int shortestBridge(vector<vector<int>>& grid) {
        a = grid;
        n = a.size();
        findFirstIsland();

        int steps = 0;
        while(!bfs.empty()) {
            int bfs_size = bfs.size();
            for(int i = 0; i < bfs_size; i++) {
                pair<int, int> current = bfs.front();
                bfs.pop();
                for(auto& dir : directions) {
                    int ni = current.first + dir.first;
                    int nj = current.second + dir.second;
                    if(ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        if(a[ni][nj] == 1) {
                            return steps;
                        } else if(a[ni][nj] == 0) {
                            a[ni][nj] = 2;
                            bfs.push({ni, nj});
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
};