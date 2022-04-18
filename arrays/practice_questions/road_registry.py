#make sure that the road system is convenient and there will be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.

def solution(roadRegister):
    if roadRegister == None or len(roadRegister) == 0:
        return True
        
    for i in range(0, len(roadRegister)):
        if rowCount(roadRegister, i) != colCount(roadRegister, i):
            return False
    
    return True
    
def rowCount(roadRegister, row):
    row_count = 0
    for each_vertex in roadRegister[row]:
        if each_vertex == "true":
            row_count += 1
    
    print(row_count)
            
    return row_count
    
def colCount(roadRegister, col):
    col_count = 0
    for i in range(0, len(roadRegister)):
        for j in range(0, len(roadRegister[i])):
            if j == col:
                if roadRegister[i][j] == "true":
                    col_count += 1
    
    print(col_count)
    return col_count

roadRegister = [["false","true","false"], ["false","false","false"], ["true","false","false"]]

roadRegister = [["false","true","true","true","false"], ["true","false","true","true","true"], ["true","true","false","true","false"], ["true","true","true","false","true"], ["true","true","true","true","false"]]

print(solution(roadRegister))