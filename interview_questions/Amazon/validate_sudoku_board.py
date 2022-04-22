'''
Implement this Sudoku validation function:

  boolean validate(int[][] grid);
    
The 'grid' input is a Suduko grid, and the function should return true only if the grid is valid, meaning that:
 * Each row contains digits 1 to 9, each digit occurs only once
 * Each col contains digits 1 to 9, each digit occurs only once
 * Each sub-grid (3x3) contains digits 1 to 9, each digit occurs only once
 
For example, here is a valid grid which should return true:
  int[][] sudokuGrid = {
      {5,3,4,6,7,8,9,1,2},
      {6,7,2,1,9,5,3,4,8},
      {1,9,8,3,4,2,5,6,7},
      {8,5,9,7,6,1,4,2,3},
      {4,2,6,8,5,3,7,9,1},
      {7,1,3,9,2,4,8,5,6},
      {9,6,1,5,3,7,2,8,4},
      {2,8,7,4,1,9,6,3,5},
      {3,4,5,2,8,6,1,7,9};
'''

'''
Input -> list of list
Output -> Boolean -> True, False 
Assumptions -> numbers from [1-9], my grid is 9x9
Edgecases -> 
Algo ->
Complexity ->
'''

def validate_sudoku(grid):
    '''
    grid -> list of list
    return: boolean, if grid is valid sudoku board or not
    '''
    #set((1, 3))
    row = set()
    #set((2, 4))
    col = set()
    box = set()
    
    for i in range(0,9):
        for j in range(0, 9):
            val = grid[i][j]
            if val not in col:
                if (i, val) in rows or (j, val) in col or (i//3,j//3,val) in box:
                    return False
                row.add((i, curr))
                col.add((j, curr))
                box.add((i,j,curr))
    
    return True
