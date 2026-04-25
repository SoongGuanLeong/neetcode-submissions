class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(N2)
        """
        volume = 0
        for i in range(len(height)):
            leftmax = rightmax = height[i]

            for j in range(i):
                leftmax = max(leftmax, height[j])
            
            for j in range(i, len(height)):
                rightmax = max(rightmax, height[j])

            volume += min(leftmax, rightmax) - height[i]
        return volume

