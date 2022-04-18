class Solution:
    def networkDelayTime(self, times, n, k):
        edges = collections.defaultdict(list)
        
        #create an adjency list
        for u,v,w in times:
            edges[u].append((v,w))
        
        print(edges)
        
        #create a min to keep track of 
        minHeap = [(0, k)]
        visited = set()
        total_time = 0
        
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            
            if node1 in visited:
                continue
            
            visited.add(node1)
            total_time = max(total_time, weight1)
            
            for node2,weight2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (weight1 + weight2, node2))
        
        return total_time if len(visited) == n else -1
        
solution = Solution()
