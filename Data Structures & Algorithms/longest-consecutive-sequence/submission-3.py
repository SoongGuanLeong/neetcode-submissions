class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(N2)
        """
        nums_set = set(nums)
        res = 0

        for num in nums:
            cnt, curr = 0, num
            while curr in nums_set:
                cnt += 1
                curr += 1
            res = max(res, cnt)
        return res