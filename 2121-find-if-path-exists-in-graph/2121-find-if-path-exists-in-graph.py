class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def buildGraph(edges):
            graph = defaultdict(list)
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        def bfs(root):
            graph = buildGraph(edges)
            q = deque([root])
            visited = {root}

            while q:
                node = q.popleft()
                if node == destination:
                    return True
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            return False        
        return bfs(source)            


        
