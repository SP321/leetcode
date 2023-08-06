class Solution {
private:
    vector<bool> col;
    vector<bool> diag1;
    vector<bool> diag2;
    int size;
    int count;

public:
    int totalNQueens(int n) {
        size = n;
        col = vector<bool>(n, 0);
        diag1 = vector<bool>(2*n - 1, 0);
        diag2 = vector<bool>(2*n - 1, 0);
        count = 0;

        backtrack(0);
        return count;
    }

    void backtrack(int row) {
        if (row == size) {
            ++count;
            return;
        }

        for (int j = 0; j < size; ++j) {
            if (col[j] || diag1[row+j] || diag2[row-j+size-1]) {
                continue;
            }

            col[j] = diag1[row+j] = diag2[row-j+size-1] = 1;
            backtrack(row+1);
            col[j] = diag1[row+j] = diag2[row-j+size-1] = 0;
        }
    }
};