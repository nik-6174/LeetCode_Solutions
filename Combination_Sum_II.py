# Title: Combination Sum II (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/combination-sum-ii/description/


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list
        candidates.sort(reverse=True)

        i = 0
        while i < len(candidates) and candidates[i] > target:
            i += 1
        candidates = candidates[i:]

        Dict = Counter(candidates)

        def find_combination(num: int) -> List[List[int]]:
            res = []
            # check if num itself is in the dictionary
            if num in Dict:
                for _ in range(Dict[num]):
                    res.append([num])
            for i in range(1, num):
                if i in Dict and Dict[i] > 0:
                    Dict[i] -= 1
                    temp = find_combination(num - i)
                    if temp:
                        for arr in temp:
                            if i <= arr[0]: # check if the resulting array is in increasing order
                                res.append([i] + arr)
                    Dict[i] += 1
            return res

        res = []
        # remove duplicates
        for lst in find_combination(target):
            if tuple(lst) not in res:
                res.append(tuple(lst))

        return [list(tpl) for tpl in res]
