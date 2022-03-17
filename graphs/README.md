DFS
Advantages:
    DFS on a binary tree generally requires less memory than breadth-first.
    DFS can be easily implemented with recursion.
    Can be used to find valid path or all possible paths, etc
Disadvantages:
    DFS doesn’t necessarily find the shortest path to a node, while the BFS does.

Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E)
O(V+E),where V is the number of vertices and E is the number of edges. 
In case of DFS on a tree, the time complexity is O(V), where V is the number of nodes.

BFS
Advantages:
    BFS is simple to implement.
    BFS can be applied to any search problem.
    BFS does not suffer from any potential infinite loop problem compared to DFS. The infinite loop problem may cause the computer to crash, whereas DFS goes deep down searching.
    BFS will always find the shortest path if the weight on the links are uniform. So BFS is complete and optimal.
Disadvantages:
    As discussed, memory utilization is poor in BFS, so we can say that BFS needs more memory than DFS.
    BFS is a ‘blind’ search; that is, the search space is enormous. The search performance will be weak compared to other heuristic searches.