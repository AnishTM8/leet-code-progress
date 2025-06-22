# Last updated: 6/22/2025, 7:16:09 PM
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = set(nums1)
        res=[]

        for num in nums2:
            if num in common:
                res.append(num)
                common.remove(num)
        return res