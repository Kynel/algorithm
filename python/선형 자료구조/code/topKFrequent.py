class Solution(object):
    def topKFrequent1(self, nums, k):
        freq = collections.Counter(nums)
        min_heap = []
        for key in freq:
            heapq.heappush(min_heap, (-freq[key], key))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result

    def topKFrequent2(self, nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
