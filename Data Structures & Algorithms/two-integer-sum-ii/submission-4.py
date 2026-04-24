class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        O(nlogn)
        """
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            tmp = target - numbers[i]

            while l <= r:
                mid = l + (r - l) // 2

                if numbers[mid] == tmp:
                    return [i+1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

"""
while l <= r:
    mid = l + (r - l) // 2

    if found:
        return mid
    elif too_small:
        l = mid + 1
    else:
        r = mid - 1
"""