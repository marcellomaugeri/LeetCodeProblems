import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_state = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                aliveNeighbors = self.countAliveNeighbors(board, i, j)
                next_state[i][j] = self.nextCellState(aliveNeighbors, board[i][j])

        # final update of board
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = next_state[i][j]

    def countAliveNeighbors(self, board: List[List[int]], m: int, n: int):
        count = 0
        for i in range(m-1, m+2):
            for j in range(n-1, n+2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i,j) != (m,n):
                    count += board[i][j]
        return count
    
    def nextCellState(self, count: int, status: int):
        #4
        if count == 3 and status == 0:
            return 1
        #2
        elif status == 1 and 2 <= count <= 3:
            return 1
        # 1 and 3
        return 0