def reverseList1(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:

        temp = head
        head = head. next
        temp . next = prev
        prev = temp
    return prev


def reverseList2(head):
    def reverse(node, prev):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
