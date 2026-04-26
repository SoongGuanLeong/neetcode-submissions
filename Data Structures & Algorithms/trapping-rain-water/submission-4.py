class Solution:
    def trap(self, height: List[int]) -> int:
        """
        """
        n = len(height)
        if n == 0:
            return 0

        volume = 0

        l, r = 0, n - 1
        max_l = height[l]
        max_r = height[r]
        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                volume += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                volume += max_r - height[r]
        return volume