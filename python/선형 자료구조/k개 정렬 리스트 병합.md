### k개 정렬 리스트 병합

[리트코드로 풀러 가기](https://leetcode.com/problems/merge-k-sorted-lists/)

k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.

```
입력
[
    1->4->5,
    1->3->4,
    2->6
]

출력
[
    1->1->2->3->4->4->5->6
]

```

---

이 문제는 우선 순위 큐를 이용하면 쉽게 풀 수 있다.

### python의 heapq 모듈을 이용한 리스트 병합

주어진 리스트는 연결 리스트 이므로, 값만 정렬해서는 문제를 풀 수 없다.

따라서 `min heap`인 python의 `heapq`를 이용하여 리스트에 요소들을 추가(`heappush`)시킨 뒤, 차례대로 `heappop`하면 정렬된 형태로 출력된다.

1. `heapq` 모듈을 이용해 주어진 입력의 각 노드의 루트를 (node.val, index, node) 순으로 `heappush`한다.

2. 차례대로 `heappop`한 뒤, 노드들을 연결해준다.

위 과정을 코드로 구현하면 다음과 같다.

```python
def mergeKLists(self, lists):
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next
```

주의해야 할 점은, `heappop` 연산으로 노드를 연결시킨 뒤, 다음 `heappop`을 하기 전, 해당 노드의 다음 노드를 `heappush` 해야 한다는 점이다.
