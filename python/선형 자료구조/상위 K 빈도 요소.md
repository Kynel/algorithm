### 상위 K 빈도 요소

[리트코드로 풀러 가기](https://leetcode.com/problems/top-k-frequent-elements/)

가장 빈번한 k개의 요소를 반환하라.

```
입력
nums = [1, 1, 1, 2, 2, 3]
k = 2

출력
[1, 2]
```

---

### Counter 사용

`Counter` 객체를 만들고, 주어진 배열을 넣게 되면 빈도수가 저장된 해시 테이블이 생성된다.

그 다음, 우선 순위 큐에 빈도수와 값을 묶어서 넣고(빈도수에 -를 붙여서 넣어야 `minheap`을 이용할 수 있다.) `heappop` 하게 되면 가장 빈도수가 높은 k 개의 결과를 얻을 수 있다.

```python
def topKFrequent(self, nums, k):
    freq = collections.Counter(nums)
    min_heap = []
    for key in freq:
        heapq.heappush(min_heap, (-freq[key], key))

    result = []

    for _ in range(k):
        result.append(heapq.heappop(min_heap)[1])

    return result
```

### Counter.most_common() 메소드 활용

위의 방식을 `Counter` 객체에서 지원하는 `most_common` 메소드를 활용해 구현해보자.

`most_common` 메소드는 빈도 수가 높은 순서대로 요소들을 출력시켜 주므로, 위에서 우선순위 큐를 이용한 부분을 대체해주면 된다.

추가적으로, `*`(패킹/언패킹), `zip` 메소드도 활용해보자.

```python
def topKFrequent(self, nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
```

위의 답을 예시를 통해 서술하자면,

`1.` `collections.Counter(nums)` 를 통하여 주어진 `nums` `list`를 `Counter` 객체로 변환한다.

- nums = [1, 1, 1, 2, 2, 2, 3], k = 2 -> counter = [(1, 3), (2, 3), (3, 1)]

`2.` `most_common(k)` 메소드를 활용해 가장 빈번한 k개의 요소를 추출한다.

- collections.Counter(nums).most_common(k) = [(1, 3), (2, 3)]

`3.` `*` (unpack)를 통해 리스트를 풀어준다.

- \*collections.Counter(nums).most_common(k) = [[1, 3], [2, 3]]

`4.` 현재 리스트는 [수, 빈도]로 저장되어 있기에, zip을 통해 필요한 정보인 '수'만 검출하고(tuple 형태로 반환됨), 리스트로 리턴해야 하므로 list()로 묶어준다.

- list(zip(\*collections.Counter(nums).most_common(k)))[0] = [1, 2]
