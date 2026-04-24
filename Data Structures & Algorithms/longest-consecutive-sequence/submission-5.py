class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        """
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                while num + cnt in nums_set:
                    cnt += 1
                res = max(res, cnt)

        return res