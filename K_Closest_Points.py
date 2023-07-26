# Title: 973. K Closest Points to Origin (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/k-closest-points-to-origin/description/

# using heap data structure
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # initialize min_heap
        heap = []

        # add the distance and the point in the heap
        for point in points:
            heapq.heappush(heap, [self.distance_from_origin(point), point])

        res = []

        # pop k times and get the points in res
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

    # find the euclidean distance from origin
    def distance_from_origin(self, coordinates: List[int]) -> int:
        return ((coordinates[0])**2 + (coordinates[1])**2)**0.5


# using just lists
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # short based on the distance and return coordinates of first k points
        return [point for point in sorted(points, key=self.distance_from_origin)[:k]]


    # find the euclidean distance from origin
    def distance_from_origin(self, coordinates: List[int]) -> int:
        return ((coordinates[0])**2 + (coordinates[1])**2)**0.5
