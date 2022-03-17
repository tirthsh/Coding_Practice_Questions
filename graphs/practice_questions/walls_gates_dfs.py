#https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/286.html
class Solution:
    def wallsAndGates(self, rooms):
        for i in range(0, len(rooms)):
            for j in range(0, len(rooms[i])):
                #if we found a gate
                if rooms[i][j] == 0:
                    #intial count is 0 bc distance from gate to gate is 0
                    self.dfs(i,j,0,rooms)
    
    #dfs search and update rooms based on distance from nearest gate
    def dfs(self, i, j, count, rooms):
        #check for out of bounds
        #last check -> if we have already found a distance thats lower than count(new distance) then don't need to traverse
            #since we're already found a shorter path to gate
        if (i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[i]) or rooms[i][j] < count):
            return
        
        #update distance to current vertex
        rooms[i][j] = count
        #call dfs on all 4 directions of rooms[i][j]
        #make sure count passed is 1 more
        self.dfs(i-1, j, count + 1, rooms)
        self.dfs(i+1, j, count + 1, rooms)
        self.dfs(i, j-1, count + 1, rooms)
        self.dfs(i, j+1, count + 1, rooms)
    
    def print(self,rooms):
        for row in rooms:
            print(row)

inf = float("inf")
rooms = [[inf, -1, 0, inf], [inf, inf, inf, -1], [inf, -1, inf, -1], [0, -1, inf, inf]]
solution = Solution()

print("Before ...")
solution.print(rooms)

solution.wallsAndGates(rooms)

print("After ...")
solution.print(rooms)
