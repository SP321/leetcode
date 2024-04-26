class Solution {
public:
    vector<int> small2(const vector<int>& a) {
        vector<int> ans(2);
        int x = INT_MAX;
        int y = INT_MAX;

        for (int i = 0; i < a.size(); ++i) {
            if (a[i] < x) {
                y = x;
                ans[1] = ans[0];
                x = a[i];
                ans[0] = i;
            } else if (a[i] < y) {
                y = a[i];
                ans[1] = i;
            }
        }
        return ans;
    }
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n=grid.size();
        for(int i=1;i<n;i++){
            vector<int>o=small2(grid[i-1]);
            for(int j=0;j<n;j++){
                grid[i][j]+=(j==o[0])?grid[i-1][o[1]]:grid[i-1][o[0]];
            }
        }
        return *min_element(grid[n-1].begin(),grid[n-1].end());
    }
};