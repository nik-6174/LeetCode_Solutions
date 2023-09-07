# Title: 82. Remove Duplicates from Sorted List II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

## Solution without modifying the values of nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=101, next=head)
        node = dummy
        
        while node:
            if node.next:
                if not node.next.next:
                    break
                else:
                    if node.next.val != node.next.next.val:
                        node = node.next
                    else:
                        val = node.next.val
                        next_node = node.next
                        while next_node and next_node.val == val:
                            next_node = next_node.next
                        node.next = next_node
            else:
                break

        return dummy.next


## Solution by modifying the node values
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        values = defaultdict(int)
        while node:
            values[node.val] += 1
            node = node.next
        unique_values = [i for i in values if values[i] == 1]
        dummy = ListNode(val=0, next=head)
        node = dummy
        for unique_value in unique_values:
            node.next.val = unique_value
            node = node.next
        node.next = None
        return dummy.next
