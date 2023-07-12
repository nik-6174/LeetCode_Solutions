# Title: 933. Number of Recent Calls (LeetCode)
# Difficulty: Easy
# Problem: https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter:

    def __init__(self):
        # initialize the queue
        self.queue = deque([])
        
    def ping(self, t: int) -> int:
        while self.queue: # while the queue is not empty
            if self.queue[0] < t - 3000:
                self.queue.popleft() # pop the queue from the left
            else:
                break
        self.queue.append(t) # append the new alement in the queue
        return len(self.queue) # return the number of requests in the last 3000 ms
        
        
        
