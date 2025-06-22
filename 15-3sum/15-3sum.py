# Last updated: 6/22/2025, 7:16:29 PM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and right != len(nums)-1 and nums[right] == nums[right + 1]:
                        right -= 1
        return res
        