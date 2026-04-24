class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        O(N2)
        """
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                total = numbers[i] + numbers[j]
                if total == target:
                    return [i + 1, j + 1]