# Title: 1235. Maximum Profit in Job Scheduling
# Difficulty: Hard
# Problem: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        dp = [0] * (len(jobs) + 1)
        
        for i in range(1, len(jobs) + 1):
            curr_profit = jobs[i - 1][2]
            prev_job_idx = bisect.bisect_right(end_times, jobs[i - 1][0])
            
            dp[i] = max(dp[i - 1], curr_profit + dp[prev_job_idx])
        
        return dp[-1]
