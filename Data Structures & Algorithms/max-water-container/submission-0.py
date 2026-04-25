class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        O(N2)
        """
        a_max = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                a = min(heights[i], heights[j]) * abs(i - j)

                a_max = max(a_max, a) 
        return a_max