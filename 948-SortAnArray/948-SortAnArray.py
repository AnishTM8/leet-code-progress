# Last updated: 3/18/2026, 9:04:04 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       return self.mergeSort(nums)
    
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        
        m = len(arr) // 2
        left = self.mergeSort(arr[:m])
        right = self.mergeSort(arr[m:])

        i = j = 0
        sorted_array = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array


