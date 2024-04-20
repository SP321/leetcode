class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int n = land.size();
        int m = land[0].size();
        vector<vector<int>> ans;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (land[i][j] == 1) {
                    int x = i;
                    int y;
                    while (x < n && land[x][j] == 1) {
                        y = j;
                        while (y < m && land[x][y] == 1) {
                            land[x][y] = 0;
                            y++;
                        }
                        x++;
                    }
                    ans.push_back({i, j, x - 1, y - 1});
                }
            }
        }
        return ans;
    }
};