class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        m = len(nums)

        res = []
        for i in range(m):
            left = math.prod(nums[:i])
            right = math.prod(nums[i+1:m])
            res.append(left * right)

        return res
        