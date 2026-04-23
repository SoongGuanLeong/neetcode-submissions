class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        res = Counter(nums).most_common(k)
        return [num for num, freq in res]
