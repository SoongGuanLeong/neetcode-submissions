class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        O(nlogk)
        """
        from collections import defaultdict
        import heapq

        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1

        heap = []

        for num, freq in hmap.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
