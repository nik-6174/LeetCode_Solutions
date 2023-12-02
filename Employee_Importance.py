# Title: 690. Employee Importance
# Difficulty: Medium
# Problem: https://leetcode.com/problems/employee-importance/description/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph, visited = {}, set()
        # map the id to the employee object
        for employee in employees:
            graph[employee.id] = employee

        def find_total_importance(ID: int):
            # avoid a loop
            if ID in visited:
                return 0
            visited.add(ID)
            # find the employee
            employee = graph[ID]
            total_importance = employee.importance
            if not employee.subordinates: return total_importance

            # if there are subordinates
            for subordinate_id in employee.subordinates:
                total_importance += find_total_importance(subordinate_id)
            return total_importance
            
        return find_total_importance(id)
