class Solution:
    '''

    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #represent the course as graph adjancency list
        graph = defaultdict(list)
        #create indegree dict to keep track of the pre-req
        indegree = defaultdict(int)
        for course, preq in prerequisites: #what happend if duplicate edge?
            graph[preq].append(course)
            indegree[course] += 1

        #present the order of course by topo sort
        res = []
        q = deque()
        visitedCount = 0

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            res.append(node)
            visitedCount += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return res if visitedCount == numCourses else []




