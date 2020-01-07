# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapNodesInPairs(head: ListNode):
    stack = list()
    retHead = newHead = ListNode(0)
    count = 0
    while head:
        if 2 == count:
            first = ListNode(stack.pop())
            second = ListNode(stack.pop())
            newHead.next = first
            first.next = second
            newHead = second
            count = 0
        stack.append(head.val)
        count += 1
        head = head.next
    while stack:
        newNode = ListNode(stack.pop())
        newHead.next = newNode
        newHead = newNode
    return retHead.next


def swapNodesInPairsBetter(head: ListNode):
    # 这个方法的重点在于，只需要交换值，不需要换指针
    if head:
        nodeH = head
        while nodeH:
            if nodeH.next:
                temp = nodeH.next.val
                nodeH.next.val = nodeH.val
                nodeH.val = temp
                nodeH = nodeH.next.next
            else:
                nodeH = None
    return head


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    # n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    # n4.next = n5

    h = swapNodesInPairsBetter(n1)
    s = ''
    while h:
        s = s + str(h.val)
        s += ' -> '
        h = h.next
    print(s)
