class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        res = [0] * len(nums)

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return res
        
        for i, num in enumerate(nums):
            if zero_cnt == 1:
                if num == 0:
                    res[i] = prod
            else:
                res[i] = int(prod / num)

        return res
