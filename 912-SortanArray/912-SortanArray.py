# Last updated: 3/10/2026, 12:54:45 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3       return self.mergeSort(nums)
4    
5    def mergeSort(self, arr):
6        if len(arr) == 1:
7            return arr
8        
9        m = len(arr) // 2
10        left = self.mergeSort(arr[:m])
11        right = self.mergeSort(arr[m:])
12
13        i = j = 0
14        sorted_array = []
15
16        while i < len(left) and j < len(right):
17            if left[i] < right[j]:
18                sorted_array.append(left[i])
19                i += 1
20            else:
21                sorted_array.append(right[j])
22                j += 1
23        
24        sorted_array.extend(left[i:])
25        sorted_array.extend(right[j:])
26
27        return sorted_array
28
29
30