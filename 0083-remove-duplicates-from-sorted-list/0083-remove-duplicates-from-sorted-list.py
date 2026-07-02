# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values =  []
        current = head 
        while current:
            if not values or values[-1] != current.val:
                values.append(current.val)
            current = current.next
        new_head = ListNode(values[0])
        current = new_head

        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return new_head