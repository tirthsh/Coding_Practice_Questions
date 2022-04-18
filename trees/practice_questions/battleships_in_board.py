#https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board):
        if board == None or len(board) == 0:
            return 0
        
        ship_count = 0
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                #increment count by 1 if we see a ship
                #recurse on its surroundings
                if board[i][j] == "X":
                    ship_count += 1
                    self.recursive_call(i,j,board)
        
        return ship_count
    
    def recursive_call(self, i, j, board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "X":
            return None
        
        #make the X -> . so we don't go over it again
        board[i][j] = "."
        self.recursive_call(i-1, j, board)
        self.recursive_call(i, j-1, board)
        self.recursive_call(i+1, j, board)
        self.recursive_call(i, j+1, board)
             

solution = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

print(solution.countBattleships(board))