class Solution {
public:
    vector<int> goodSubsetofBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        unordered_set<int> s;
        unordered_map<int, int> ind;

        for (int i = 0; i < n; i++) {
            int x = 0;
            for (int j = 0; j < grid[i].size(); j++) {
                x = (x << 1) | grid[i][j];
            }
            s.insert(x);
            ind[x] = i;
        }

        vector<int> gr(s.begin(), s.end());
        n = gr.size();

        for (int i = 0; i < n; i++) {
            int x = gr[i];
            if (x == 0) {
                return {ind[x]};
            }
        }

        for (int i = 0; i < n; i++) {
            int x = gr[i];
            for (int j = i + 1; j < n; j++) {
                int y = gr[j];
                if ((x & y) == 0) {
                    return {min(ind[x], ind[y]), max(ind[x], ind[y])};
                }
            }
        }

        return {};
    }
};