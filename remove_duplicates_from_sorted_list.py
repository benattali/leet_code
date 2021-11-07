# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
one = ListNode(1)
two = ListNode(2)
head.next = one
one.next = two


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        curNode = head

        while curNode.next:
            nextNode = curNode.next
            if curNode.val == nextNode.val:
                curNode.next = nextNode.next
            else:
                curNode = nextNode

        return head


Solution().deleteDuplicates(head)
