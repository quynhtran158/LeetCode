from collections import defaultdict, deque
class Solution:
    '''
    is this a DAG graph? will it has cycle? ex: [1,0] and [0,1]? -> yes it can have cycle

    - present the relationship between pre-req and the course as a graph of adjency list
    directed graph:
    node as the course
    edge directed: as the the pre-req to the course (bi to ai) (ex: [0, 1] 1 is the pre-req, 1 -> 0)
    - check whether the graph has cycle, if has cycle -> return False immediately (DFS)
    - do topological sort to sort the course to determine the order in which all of the course can be finished
    + keep track of the indegree of each node
    + repeatedly visite the node with 0 indegee, delete all edge associated with it -> decreamen of neighbor indegee edge


    step:
    1/ create a graph as adjancy list to represent the course
    2/ have indegree list to store the indeegee of each node (course)
    3/ have a queue to add the 0-indegee node to decrease the indegee of neighbor node
    4/ at the end, if all node with 0 indegee processed ( proccessedCount == n) return true, if  proccessedCount != n -> has cycle - return false
    '''
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
            

