# Title: 2462. Total Cost to Hire K Workers
# Difficulty: Medium
# Problem: https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

## Solution 1
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) < 2 * candidates + k:
            return sum(sorted(costs)[:k])
        
        # initialized the two pointers
        pointer1, pointer2, n = candidates, len(costs) - 1 - candidates, len(costs)

        # fill the two heaps
        heap1, heap2 = [(i, j) for j, i in enumerate(costs[:pointer1])], [(costs[i+pointer2+1], i+pointer2+1) for i in range(candidates)]
        heapq.heapify(heap1)
        heapq.heapify(heap2)

        # result
        res = set()

        # store the minimum from the two heaps
        (min1, idx1), (min2, idx2) = heapq.heappop(heap1), heapq.heappop(heap2)

        while len(res) < k:
            # compare the add the minimum element with least index
            if min1 <= min2:
                # add the new index
                res.add(idx1)
                if pointer1 < n:
                # push the new element, then pop
                    min1, idx1 = heapq.heappushpop(heap1, (costs[pointer1], pointer1))
                    pointer1 += 1
                else:
                    if heap1: # if heap not empty
                        min1, idx1 = heapq.heappop(heap1)
                    else: # only pop from heap2 now
                        min1 = float('inf')
            else:
                # add the new index
                res.add(idx2)
                if pointer2 >= 0:
                    min2, idx2 = heapq.heappushpop(heap2, (costs[pointer2], pointer2))
                    pointer2 -= 1
                else:
                    if heap2: # if heap is non empty
                        min2, idx2 = heapq.heappop(heap2)
                    else: # only pop from heap1 now
                        min2 = float('inf')

        return sum([costs[i] for i in res]) # sum of all values of unique indexes

## Solution 2 (most efficient)

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) ->int:
        length = len(costs)
        if length < 2 * candidates + k: return sum(sorted(costs)[:k])

        answer, headQ, tailQ = 0, costs[:candidates], costs[-candidates:]
        heapify(headQ); heapify(tailQ)

        next_head, next_tail = candidates, length - 1 - candidates

        for _ in range(k):
            if headQ[0] <= tailQ[0]:
                # heapreplace will pop/return the smallest item then push new item
                answer += heapreplace(headQ, costs[next_head])
                next_head += 1
            else:
                answer += heapreplace(tailQ, costs[next_tail])
                next_tail -= 1
        return answer
