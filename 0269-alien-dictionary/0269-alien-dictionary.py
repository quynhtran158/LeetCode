class Solution:
    '''
    - use the alien lexicographical order to return the word 
    but, if have multiple valid order, return the smallest lexicographical order (ASCII)
    => use heap to get the smallest order (ASCII based not alien)

    - rule of lexicographical order by alien:
     + the first different of first word become before the 1st letter of second word 
     ("wrt","wrf")  r -> f because r and f are the first diff letter

     ("ett","rftt") e -> r because e and r are the first diff letters

    step:
    1/ iterate the words list to decide the order of the lette by alien lexicographcal order
    2/ reperesent the alien order into directed graph as adjaceny list
        node: as the first different char
        edge: the order constains follow alien lexicographical order
    3/ compute indegree of each node
    4/ use heap to return the smallest lexicographical order in multiple valid order by using topological sort

    '''
    def buildGraph(self, words):
        graph = defaultdict(list)
        for word in words:
            for char in word:
                graph[char]  # Ensure all characters exist
                #Some characters may never appear in a comparison (i.e., they never have edges).
                #We still need to include them in the graph to ensure they appear in the final ordering.         
                '''
                words = ["abc", "acd"]
                Characters {a, b, c, d} exist.
                'b' and 'd' may never appear as a starting character in an edge.
                This loop ensures every character exists as a node in the graph.
                '''
        prev = words[0] #store the first word as prev, will use in comparision with next word
        for i in range(1, len(words)): #i keep track of the order word in words
            curr = words[i]
            j = 0
            foundDiff = False
            while j < len(prev) and j < len(curr): #function find the first diff char in word
                #ignore duplicate
                if prev[j] != curr[j]:
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].append(curr[j])
                    foundDiff = True
                    break #stop early after find the first diff, the rest doesnt matter
                j += 1 #move to next index if the word is the same in both prev[j] and curr[j]
            
            if len(prev) > len(curr) and not foundDiff:
                return None
            prev = curr #move to the next word in words after found the first diff char 
        return graph         
        
    def findIndegree(self, graph):
        indegree = defaultdict(int)
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    def topoSort(self, graph):
        res = []
        pq = [] #heap
        indegree = self.findIndegree(graph)

        for node in graph:
            if indegree[node] == 0:
                heappush(pq,node)
                
        while pq:
            node = heappop(pq)
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(pq, neighbor)
        return res if len(res) == len(graph)else None #len == is DAG no cycle, len != there are node has no 0 indegree -> cycle
 
    def alienOrder(self, words: List[str]) -> str:
        graph = self.buildGraph(words)
        if not graph:
            return ""
        order = self.topoSort(graph)
        return "" if order is None else "".join(order)