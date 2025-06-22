# Last updated: 6/22/2025, 7:16:04 PM
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        num_to_count = defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                num_to_count[num1 + num2] += 1
        
        result = 0

        for num3 in nums3:
            for num4 in nums4:
                result += num_to_count[-(num3+num4)]
        return result