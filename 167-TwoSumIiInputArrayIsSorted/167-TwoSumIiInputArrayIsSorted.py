# Last updated: 6/22/2025, 7:16:18 PM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1