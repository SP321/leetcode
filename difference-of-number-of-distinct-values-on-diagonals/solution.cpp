
class Solution {
public:
    vector<vector<int>> differenceOfDistinctValues(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        this->grid = grid;

        vector<vector<int>> grid_ans(n, vector<int>(m, 0));
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                grid_ans[i][j] = abs(sum_tl(i, j) - sum_br(i, j));
            }
        }
        return grid_ans;
    }
    int n;
    int m;
    vector<vector<int>> grid;

    int sum_tl(int i, int j){
        set<int> s;
        i--;
        j--;
        while(i>=0 && j>=0) {
            s.insert(grid[i][j]);
            i--;
            j--;
        }
        return s.size();
    };

    int sum_br(int i, int j){
        set<int> s;
        i++;
        j++;
        while(i<n && j<m) {
            s.insert(grid[i][j]);
            i++;
            j++;
        }
        return s.size();
    };
};