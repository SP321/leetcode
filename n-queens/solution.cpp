class Solution {
private:
    vector<vector<string>> ans;
    vector<string> board;
    vector<bool> cols;
    vector<bool> diag1;
    vector<bool> diag2;
    int n;

public:
    vector<vector<string>> solveNQueens(int n) {
        this->n = n;
        ans.clear();
        board = vector<string>(n, string(n, '.'));
        cols = vector<bool>(n, false);
        diag1 = vector<bool>(2 * n - 1, false);
        diag2 = vector<bool>(2 * n - 1, false);

        dfs(0);
        return ans;
    }

    void dfs(int i) {
        if (i == n) {
            ans.push_back(board);
            return;
        }

        for (int j = 0; j < n; j++) {
            if (cols[j] || diag1[i + j] || diag2[j - i + n - 1]) continue;
            cols[j] = diag1[i + j] = diag2[j - i + n - 1] = true;
            board[i][j] = 'Q';
            dfs(i + 1);
            cols[j] = diag1[i + j] = diag2[j - i + n - 1] = false;
            board[i][j] = '.';
        }
    }
};