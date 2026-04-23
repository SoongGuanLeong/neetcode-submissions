class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1

        hmap = sorted(hmap.items(), key= lambda x: x[1], reverse=True)

        res = [num for num, freq in hmap[:k]]

        return res