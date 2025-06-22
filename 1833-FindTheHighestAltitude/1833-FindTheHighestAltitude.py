# Last updated: 6/22/2025, 7:15:44 PM
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum = 0
        output = [0] * len(gain)

        for i in range(len(gain)):
            output[i] = prefix_sum
            prefix_sum += gain[i]
        output.append(prefix_sum)
        return max(output)