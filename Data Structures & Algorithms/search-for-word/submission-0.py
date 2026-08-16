class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [[False for _ in row] for row in board]

        def backtrack(i, j, index):

            if index == len(word):
                return True

            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False

            if visited[i][j]:
                return False

            if board[i][j] != word[index]:
                return False

            visited[i][j] = True

            res = (
                backtrack(i, j - 1, index + 1) or
                backtrack(i, j + 1, index + 1) or 
                backtrack(i - 1, j, index + 1) or 
                backtrack(i + 1, j, index + 1)
            )

            visited[i][j] = False

            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False