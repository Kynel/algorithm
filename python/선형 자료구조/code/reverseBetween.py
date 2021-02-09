def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if n == m:
        return head
    
    root = start = ListNode(None)
    root.next = head
    for _ in range(m - 1):
        start = start.next
    end = start.next
    
    for _ in range(n - m):
        temp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = temp
    
    return root.next