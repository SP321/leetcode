class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        n = len(empty_cells)

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grids[(i // 3) * 3 + j // 3].add(board[i][j])

        def get_options(x, y):
            all_nums = set(str(i) for i in range(1,10))
            used_nums = rows[x].union(cols[y]).union(grids[(x // 3) * 3 + y // 3])
            return list(all_nums - used_nums)

        def backtrack(i):
            nonlocal empty_cells
            if i == n:
                return True
            empty_cells[i:] = sorted(empty_cells[i:], key=lambda a: len(get_options(*a)))
            x, y = empty_cells[i]
            options = get_options(x, y)
            random.shuffle(options)
            for option in options:
                board[x][y] = option
                rows[x].add(option)
                cols[y].add(option)
                grids[(x // 3) * 3 + y // 3].add(option)
                if backtrack(i + 1):
                    return True
                board[x][y] = '.'
                rows[x].remove(option)
                cols[y].remove(option)
                grids[(x // 3) * 3 + y // 3].remove(option)
            return False
        
        backtrack(0)