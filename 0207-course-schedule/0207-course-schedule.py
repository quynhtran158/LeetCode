from collections import defaultdict, deque
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        #create indegee list
        indegree = defaultdict(int)
        #create graph as adjacency list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        #queue for 0 indegee node
        q = deque([prereq for prereq in range(numCourses) if indegree[prereq] == 0])
        processedCount = 0

        #process node in topo sort order:
        while q:
            node = q.popleft()
            processedCount += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return processedCount == numCourses
            

