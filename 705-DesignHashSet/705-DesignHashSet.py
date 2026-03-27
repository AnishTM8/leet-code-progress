# Last updated: 3/27/2026, 5:56:18 PM
1class ListNode:
2    def __init__(self, key):
3        self.key = key
4        self.next = None
5
6class MyHashSet:
7
8    def __init__(self):
9        self.set =[ListNode(0) for i in range(10**4)]
10
11    def add(self, key: int) -> None:
12        index = key%len(self.set)
13        curr = self.set[index]
14
15        while curr.next:
16            if curr.next.key == key:
17                return
18            curr = curr.next
19        curr.next = ListNode(key)    
20            
21
22    def remove(self, key: int) -> None:
23        index = key%len(self.set)
24        curr = self.set[index]
25
26        while curr.next:
27            if curr.next.key == key:
28                curr.next = curr.next.next
29                return
30            curr = curr.next
31
32    def contains(self, key: int) -> bool:
33        index = key%len(self.set)
34        curr = self.set[index]
35
36        while curr.next:
37            if curr.next.key == key:
38                return True
39            curr = curr.next
40        return False
41
42# Your MyHashSet object will be instantiated and called as such:
43# obj = MyHashSet()
44# obj.add(key)
45# obj.remove(key)
46# param_3 = obj.contains(key)