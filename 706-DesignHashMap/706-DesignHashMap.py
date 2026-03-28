# Last updated: 3/28/2026, 12:32:29 PM
1class ListNode:
2    def __init__(self, key = -1, val = -1):
3        self.key = key
4        self.next = None
5        self.val = val     
6
7class MyHashMap:
8
9    def __init__(self):
10        self.map = [ListNode() for i in range(10**4)]
11
12    def put(self, key: int, value: int) -> None:
13        index = key%len(self.map)
14        curr = self.map[index]
15
16        while curr.next:
17            if curr.next.key == key:
18                curr.next.val = value
19                return
20            curr = curr.next
21        
22        curr.next = ListNode(key,value)
23        
24
25    def get(self, key: int) -> int:
26        index = key%len(self.map)
27        curr = self.map[index]
28
29        while curr.next:
30            if curr.next.key == key:
31                return curr.next.val
32            curr = curr.next
33        return -1        
34
35    def remove(self, key: int) -> None:
36        
37        index = key%len(self.map)
38        curr = self.map[index]
39
40        while curr.next:
41            if curr.next.key == key:
42                curr.next = curr.next.next
43                return
44            curr = curr.next
45
46# Your MyHashMap object will be instantiated and called as such:
47# obj = MyHashMap()
48# obj.put(key,value)
49# param_2 = obj.get(key)
50# obj.remove(key)