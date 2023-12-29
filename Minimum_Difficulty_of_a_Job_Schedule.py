# TItle: 1335. Minimum Difficulty of a Job Schedule
# Difficulty: Hard
# Problem: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ## solution using DP, using cache decorator
        n = len(jobDifficulty)
        # not enough jobs for each day
        if n < d:
            return -1
        
        @functools.lru_cache(None)
        def dp(jobs_left: int, days_left: int):
            if days_left == 1:
                return max(jobDifficulty[-jobs_left:])
            difficulty = jobDifficulty[-jobs_left]
            jobs_left -= 1
            days_left -= 1
            # total minumum difficulty for last days_left days
            total_difficulty = difficulty + dp(jobs_left, days_left)

            # increase the number of difficult tasks for today
            while jobs_left > days_left:
                difficulty = max(difficulty, jobDifficulty[-jobs_left])
                jobs_left -= 1
                total_difficulty = min(total_difficulty, difficulty + dp(jobs_left, days_left))

            return total_difficulty

        return dp(n, d)
