class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        """
        a_max = 0
        for i in range(len(heights)):
            l = i
            r = len(heights) - 1

            while i < r:
                a = min(heights[l], heights[r]) * abs(l - r)
                a_max = max(a_max, a)

                if heights[l] == heights[r]:
                    break
                elif heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1
        return a_max



"""

=======================
two pointers template
=======================
nums.sort()

l = 0
r = len(nums) - 1

while l < r:
    current = nums[l] + nums[r]

    if current == target:
        # process answer

        l += 1
        r -= 1

    elif current < target:
        l += 1

    else:
        r -= 1
"""
        