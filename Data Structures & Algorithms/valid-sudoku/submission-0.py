class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == ".":
                    continue
                else:
                    i = (r // 3, c // 3)
                    num = i[0] * 3 + i[1]
                    if (int(cell) in rows[r]) or (int(cell) in cols[c]) or (int(cell) in boxes[num]):
                        return False
                    else:
                        rows[r].add(int(cell))
                        cols[c].add(int(cell))
                        boxes[num].add(int(cell))
        return True