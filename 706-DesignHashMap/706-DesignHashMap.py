# Last updated: 3/9/2026, 7:59:33 PM
1class ListNode:
2    def __init__(self, key= -1, val = -1, next = None):
3        self.key = key
4        self. val = val
5        self.next = next
6class MyHashMap:
7
8    def __init__(self):
9        self.map = [ListNode() for i in range(10**4)]
10
11    def put(self, key: int, value: int) -> None:
12        index = key%len(self.map)
13        curr = self.map[index]
14
15        while curr.next:
16            if curr.next.key == key:
17                curr.next.val = value
18                return
19            curr = curr.next
20        curr.next = ListNode(key, value)
21        
22    def get(self, key: int) -> int:
23        index = key%len(self.map)
24        curr = self.map[index]
25
26        while curr.next:
27            if curr.next.key == key:
28                return curr.next.val
29            curr = curr.next
30        return -1
31
32    def remove(self, key: int) -> None:
33        index = key%len(self.map)
34        curr = self.map[index]
35
36        while curr.next:
37            if curr.next.key == key:
38                curr.next = curr.next.next
39                return
40            curr = curr.next
41
42
43# Your MyHashMap object will be instantiated and called as such:
44# obj = MyHashMap()
45# obj.put(key,value)
46# param_2 = obj.get(key)
47# obj.remove(key)