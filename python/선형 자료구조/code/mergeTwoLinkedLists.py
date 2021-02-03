def mergeTwoLists1(self, l1, l2):
    # 1. l1이 None이면, l1과 l2를 무조건 바꾸어야 함
    # 2. 이때, l2가 None이면 바꾸면 안됨
    # 3. l1, l2 노드의 값이 작은 쪽이 l1가 됨
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    # 이렇게 바꾸었을 때, l1이 None이면 l1, l2둘다 None임
    # 둘다 None이라면 재귀를 더이상 하면 안되기에, if로 체크함
    if l1:
        # l1이 존재하면, l1의 next를 찾기 위한 재귀를 실행
        l1.next = mergeTwoLists(l1.next, l2)

    return l1


def mergeTwoLists2(self, l1, l2):
    result = ListNode()
    current = result

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1

    elif l2:
        current.next = l2

    return result.next
