class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                else: seen.add(board[row][col])

        # check col
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[col][row] == ".":
                    continue
                if board[col][row] in seen:
                    return False
                else: seen.add(board[col][row])

        # check 3x3 box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
