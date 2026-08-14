class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                val = board[i][j]
                if val != ".":

                    box_row = (i // 3)
                    box_col = (j // 3)
                    index = box_row * 3 + box_col

                    if val in rows[i] or val in cols[j] or val in boxes[index]:
                        return False

                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[index].add(board[i][j])
        return True