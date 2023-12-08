# Title: 207. Course Schedule
# Difficulty: Medium
# Problem: https://leetcode.com/problems/course-schedule/description

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course1, course2 in prerequisites:
            graph[course1].append(course2)

        def hasCycle(course, visited):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1
            for dep_course in graph[course]:
                if hasCycle(dep_course, visited):
                    return True

            visited[course] = 2
            return False

        visited = [0] * numCourses
        for course in range(numCourses):
            if hasCycle(course, visited):
                return False
        return True
