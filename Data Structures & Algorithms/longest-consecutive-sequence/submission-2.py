class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(nlogn)
        """
        if not nums:
            return 0

        nums = sorted(set(nums))
        cnt = 1
        res = 1

        prev = nums[0]
        for num in nums[1:]:

            if num == prev + 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
            prev = num
        
        return max(res, cnt)
            
