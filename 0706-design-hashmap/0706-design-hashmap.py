class ListNode:
    def __init__(self, key):
        self.key = key
        # self.value = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.set = [ListNode([]) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key[0] == key:
                cur.next.key[1] = value
                return 
            cur = cur.next
        cur.next = ListNode([key, value])
    def get(self, key: int) -> int:
        cur = self.set[key % len(self.set)]
        # print(self.set[key % len(self.set)].key)
        while cur.next:
            if cur.next.key[0] == key:
                # print(cur.next.key)
                return cur.next.key[1]
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key[0] == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)