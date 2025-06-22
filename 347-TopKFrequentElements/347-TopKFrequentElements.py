# Last updated: 6/22/2025, 7:16:10 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            freq[value].append(key) 
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for lis in freq[i]:
                res.append(lis)
                if len(res) == k:
                    return res