# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
       
        #Convert to Array Method:
        current_node = head
        array = []
        while current_node:
            array.append(current_node.val)
            current_node=current_node.next
        return array == array[::-1]
