# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return ListNode().next
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            merged_list = ListNode(list1.val)
            list1 = list1.next
        else:
            merged_list = ListNode(list2.val)
            list2 = list2.next

        while list1:
            if not list2:
                self.findTail(merged_list).next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                self.findTail(merged_list).next = ListNode(list1.val)
                list1 = list1.next
            else:
                self.findTail(merged_list).next = ListNode(list2.val)
                list2 = list2.next

        while list2:
            self.findTail(merged_list).next = ListNode(list2.val)
            list2 = list2.next

        self.printList(merged_list)
        return merged_list

    def printList(self, linked_list):
        if linked_list == None:
            return
        print(linked_list.val)
        self.printList(linked_list.next)

    def findTail(self, linked_list):
        while linked_list.next:
            linked_list = linked_list.next
        return linked_list


h_1 = ListNode(1)
h1_2 = ListNode(2)
h1_4 = ListNode(4)
h_1.next = h1_2
h1_2.next = h1_4

h_2 = ListNode(1)
h1_3 = ListNode(3)
h1_4 = ListNode(4)
h_2.next = h1_3
h1_3.next = h1_4

Solution().mergeTwoLists(h_1, h_2)
