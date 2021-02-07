def swapPairs1(self, head):

    if not (head and head.next):
        return head

    node = head
    while node and node.next:
        node.val, node.next.val = node.next.val, node.val
        node = node.next.next

    return head


def swapPairs2(self, head):
    root_node = prev = ListNode(None)
    prev.next = head
    current_node = head

    while current_node and current_node.next:
        next_node = current_node.next
        current_node.next = next_node.next
        next_node.next = current_node

        prev.next = next_node

        current_node = current_node.next
        prev = prev.next.next

    return root_node.next


def swapPairs3(self, head):
    if head and head.next:
        p = head.next

        head.next = self.swapPairs(p.next)
        p.next = head
        return p

    return head
