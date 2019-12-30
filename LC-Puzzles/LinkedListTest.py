# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = list()
        start = head
        length = 0
        while start:
            stack.append(start)
            start = start.next
            length += 1
        if 0 == n:
            return head
        if 1 == n:
            if length == n:
                return None
            else:
                pre = stack[length - 2]
                pre.next = None
        elif length == n:
            post = stack[1]
            head = post
        else:
            post = stack[length - n + 1]
            pre = stack[length - n - 1]
            pre.next = post
        return head

    '''
    想象一下，两个人进行 100m 赛跑，假设他们的速度相同。开始的时候，第一个人就在第二个人前边 10m ，这样当第一个人跑到终点的时候，
    第二个人相距第一个人依旧是 10m ，也就是离终点 10m。
    对比于链表，我们设定两个指针，先让第一个指针遍历 n 步，然后再让它俩同时开始遍历，这样的话，当第一个指针到头的时候，第二个指针
    就离第一个指针有 n 的距离，所以第二个指针的位置就刚好是倒数第 n 个结点。
    '''

    def removeNthFromEndBetter(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # 第一个指针先移动 n 步
        for i in range(0, n + 1):
            first = first.next

        # 第一个指针移动至链表末端，第二个指针也会同时移动
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


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

    s = Solution()
    h = s.removeNthFromEndBetter(n1, 4)
    s = ''
    while h:
        s = s + str(h.val)
        s += ' -> '
        h = h.next
    print(s)
