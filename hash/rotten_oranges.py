class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
    
        fresh_coor = []
        rotten_coor = []
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                val = grid[i][j]
                print(val)
                if val == 2:
                    rotten_coor.append([i,j])
                elif val == 1:
                    fresh_coor.append([i,j])
        
        if len(fresh_coor) == 0:
            return 0
        
        surrounding_coor = [[1,0], [-1,0], [0,1], [0,-1]]
        minute_count = 0
        
        left_to_visit = rotten_coor
        print(left_to_visit)
        
        while len(left_to_visit):
            for visiting in left_to_visit:
                rotten_orange = [visiting[0],visiting[1]]
                for each_direction in surrounding_coor:
                    direction_coor = [rotten_orange[0]+each_direction[0], rotten_orange[1]+each_direction[1]]
                    i = direction_coor[0]
                    j = direction_coor[1]

                    if ([i,j] in fresh_coor):
                        grid[i][j] = 2
                        rotten_coor.append([i,j])
                        left_to_visit.append([i,j])
                        fresh_coor.remove([i,j])
                left_to_visit.remove(visiting)
      
            minute_count += 1

        if len(fresh_coor) != 0:
            return -1
        
        return minute_count
        
        