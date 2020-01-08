# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroups(head: ListNode, k: int):
    stack = list()
    retHead = newHead = ListNode(0)
    count = 0
    while head:
        if k == count:
            while stack:
                newNode = ListNode(stack.pop())
                newHead.next = newNode
                newHead = newNode
            count = 0
        stack.append(head.val)
        count += 1
        head = head.next
    while stack:
        if k == count:
            newNode = ListNode(stack.pop())
        else:
            newNode = ListNode(stack.pop(0))
        newHead.next = newNode
        newHead = newNode
    return retHead.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    # n6 = ListNode(6)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    # n5.next = n6

    h = reverseKGroups(n1, 2)
    s = ''
    while h:
        s = s + str(h.val)
        s += ' -> '
        h = h.next
    print(s)
