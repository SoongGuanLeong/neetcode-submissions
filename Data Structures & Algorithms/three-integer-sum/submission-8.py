class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(N2)
        """
        from collections import Counter

        nums.sort()
        hmap = Counter(nums)
        res = []

        for i in range(len(nums)):
            hmap[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i+1, len(nums)):
                hmap[nums[j]] -= 1
                if j - 1> i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])

                if hmap[target] > 0:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i + 1, len(nums)):
                hmap[nums[j]] += 1

        return res