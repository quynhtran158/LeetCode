class Solution:
    '''
    build graph to represent the edge and node
    has isCommon to prevent duplicate count edge between 2 node
    count indgree of any 2 node, try to compare each pair of city to find the max
    maxRank = indegree node of each city - commond edge

    can we consider the cities that are not connected?
    store common edge ntn?
  
    '''
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        def buildGraph(roads):
            isConnected = [True]
            graph = defaultdict(list)
            for a, b in roads:
                graph[a].append(b)
                graph[b].append(a)
            return graph
        
        indegree = defaultdict(int)
        maxRank = 0
        graph = buildGraph(roads)
        for a, b in roads:
            indegree[a] += 1
            indegree[b] += 1
             # Compare each pair of cities (i, j)
        for i in range(n):
            for j in range(i + 1, n):  # Ensure i != j
                # Calculate the common edge count (1 if there's a road between i and j)
                common_edge = 1 if j in graph[i] else 0
                # Calculate the network rank for the pair (i, j)
                network_rank = indegree[i] + indegree[j] - common_edge
                # Update the maxRank if the current pair's rank is greater
                maxRank = max(maxRank, network_rank)
        return maxRank
        
        

        
        
  




        


        