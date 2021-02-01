def isPalindrome(head):
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        reverse, reverse.next, slow = slow, reverse, slow.next

    if fast:
        slow = slow.next

    while reverse and (reverse.val == slow.val):
        slow, reverse = slow.next, reverse.next
    return not reverse
