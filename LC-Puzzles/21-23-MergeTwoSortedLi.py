from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoSortedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mover = newHead = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                mover.next = l1
                l1 = l1.next
            else:
                mover.next = l2
                l2 = l2.next
            mover = mover.next
        mover.next = l2 or l1
        return newHead.next

    def mergeKSortedLists(self, lists: list[ListNode]) -> ListNode:
        if len(lists) == 0:
            return ListNode(0).next
        if len(lists) == 1:
            return lists[0]
        else:
            return self.mergeTwoSortedLists(lists[0], self.mergeKSortedLists(lists[1:]))

    def mergeKsortedLists_BruteForce(self, lists: list[ListNode]) -> ListNode:
        nodes = []
        head = pointer = ListNode(0)

        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            pointer.next = ListNode(x)
            pointer = pointer.next
        return head.next

    def mergeKsortedLists_PriorityQ_hailin(self, lists: list[ListNode]) -> ListNode:
        head = pointer = ListNode(0)
        pq = PriorityQueue()
        idx = 0
        for l in lists:
            while l:
                pq.put((l.val, idx, l))
                l = l.next
        while not pq.empty():
            val, item = pq.get()
            pointer.next = item
            pointer = pointer.next
        return head.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    h1 = ListNode(6)
    h2 = ListNode(7)
    h3 = ListNode(8)
    h4 = ListNode(9)
    h5 = ListNode(9)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5

    s = Solution()
    h = s.mergeTwoSortedLists(n1, h1)
    s = ''
    while h:
        s = s + str(h.val)
        s += ' -> '
        h = h.next
    print(s)
