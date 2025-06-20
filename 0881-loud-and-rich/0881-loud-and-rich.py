from collections import deque

class Solution:
    def buildGraph(self, nodes, edges):
        graph = {node: [] for node in nodes}
        for a, b in edges:
            graph[a].append(b)
        return graph
    
    def findIndegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node in indegree:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree
    
    def topoSort(self, graph):
        indegree = self.findIndegree(graph)
        q = deque()
        sorted_order = []

        for node in graph:
            if indegree[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return sorted_order
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        nodes = list(range(len(quiet)))
        graph = self.buildGraph(nodes, richer)
        res = [i for i in range(len(quiet))] #intialize the val of its person quietness by their order e.g. 0th per = 0
        #with this, later we can use their value as the index in the quiet array later
        sorted_order = self.topoSort(graph) #ascending order: rich to poor

        for node in sorted_order:
            for neighbor in graph[node]:
                if quiet[res[node]] < quiet[res[neighbor]]:
                    res[neighbor] = res[node] #neighbor la node poor
                    '''
                    o buoc nay da sort duoc ai giau hon cai current neighbor node roi (which is the node)
                    nen step 2 la tim node nao trong list nodes (richer) co least quiet thi bo vo cai res
                    vd: trong cai arr quiet cua de bai, tim dc least quiet value trong list node
                    thi phai add cai node do vo res de return
                    nen la the cai node vo cai cho cua neighbor trong array res, vi index = order cua graph
                    nen moi co res[neighbor] = res[node] 
                    -> nghia la node > neighbor va dam bao quietest nhat trong dam richer cua node
                    '''
        return res