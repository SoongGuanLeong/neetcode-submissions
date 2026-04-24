class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        O(N2)
        """
        row_num = len(board)
        col_num = len(board[0])

        for i in range(row_num):
            seen = set()
            for j in range(col_num):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        for j in range(col_num):
            seen = set()
            for i in range(row_num):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        for square in range(9):
            seen = set()
            start_row = square // 3 * 3
            start_col = square % 3 * 3

            for row in range(3):
                for col in range(3):
                    i = start_row + row
                    j = start_col + col

                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        return True