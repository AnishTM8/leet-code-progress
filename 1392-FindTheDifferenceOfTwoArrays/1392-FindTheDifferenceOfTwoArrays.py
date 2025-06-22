# Last updated: 6/22/2025, 7:15:53 PM
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        set1 = set(nums1) - set(nums2)
        set2 = set(nums2) - set(nums1)
        answer.append(list(set1))
        answer.append(list(set2))
        return answer
