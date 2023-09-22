class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        for idx, (x, y) in enumerate(moves):
            board[x][y] = 'A' if idx % 2 == 0 else 'B'
        
        for p in 'AB':
            if  any(
                    all(board[i][j] == p for j in range(3)) or \
                    all(board[j][i] == p for j in range(3)) \
                    for i in range(3)
                )or\
                all(board[i][i] == p for i in range(3)) or \
                all(board[i][2-i] == p for i in range(3)):
                return p

        return "Draw" if len(moves) == 9 else "Pending"