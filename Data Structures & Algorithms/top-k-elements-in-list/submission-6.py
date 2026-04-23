class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        O(N)
        """
        from collections import defaultdict

        hmap = defaultdict(int)
        res = []

        for num in nums:
            hmap[num] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, freq in hmap.items():
            buckets[freq].append(num)
        
        for bucket in reversed(buckets):
            for number in bucket:
                res.append(number)
                if len(res) == k:
                    return res
        