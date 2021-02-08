def addTwoNumbers1(self, l1, l2):
    num1 = 0
    num2 = 0

    count = 0
    while l1:
        num1 += l1.val * (10 ** count)
        count += 1
        l1 = l1.next

    count = 0

    while l2:
        num2 += l2.val * (10 ** count)
        count += 1
        l2 = l2.next

    result = str(num1 + num2)

    last = None

    for c in result:
        node = ListNode(c)
        node.next = last
        # 여기서 last가 가리키는 것을 바꾸지만, node.next는 last가 이전에 가리키고 있던 객체를 가리키기 때문에 바뀌지 않는다.
        last = node

    return node


def addTwoNumbers2(self, l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next
