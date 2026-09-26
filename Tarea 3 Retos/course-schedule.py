from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)  
            indegree[course] += 1


        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        courses_taken = 0


        while queue:
            current = queue.popleft()
            courses_taken += 1

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)


        return courses_taken == numCourses