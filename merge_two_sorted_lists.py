# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_node(self, node: ListNode) -> ListNode:
        while node.next:
            node = node.next
        return node

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return []
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        if l1.val < l2.val:
            head_val = l1.val
            l1 = l1.next
        else:
            head_val = l2.val
            l2 = l2.next
        root = ListNode(head_val)

        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                tail = self.add_node(root)
                tail.next = node
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                tail = self.add_node(root)
                tail.next = node
                l2 = l2.next

        while l1:
            node = ListNode(l1.val)
            tail = self.add_node(root)
            tail.next = node
            l1 = l1.next

        while l2:
            node = ListNode(l2.val)
            tail = self.add_node(root)
            tail.next = node
            l2 = l2.next

        return root


l1_head = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)
l1_head.next = l1_2
l1_2.next = l1_4

l2_head = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)
l2_head.next = l2_3
l2_3.next = l2_4


test = Solution().mergeTwoLists(l1_head, l2_head)
print(test)
