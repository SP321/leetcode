class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        helper(board);
    }

    bool isValid(vector<vector<char>>& board, int rowNum, int colNum, char ch) {
        for(int i = 0 ; i < 9 ; i++) {
            if(board[rowNum][i] == ch) {
                return false;
            }

            if(board[i][colNum] == ch) {
                return false;
            }

            if(board[3 * (rowNum/3) + i/3][3 * (colNum/3) + i%3] == ch) {
                return false;
            }

        }

        return true;
    }

    bool helper(vector<vector<char>>& board) {

        for(int i = 0 ; i < board.size() ; i++) {
            for(int j = 0 ; j < board[0].size() ; j++) {
                if(board[i][j] == '.') {
                    for(char k = '1' ; k <= '9' ; k++) {
                        if(isValid(board,i,j,k)) {
                            board[i][j] = k;
                            if(helper(board)) {
                                return true;
                            }
                            else {
                                board[i][j] = '.';
                            }
                            
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
};