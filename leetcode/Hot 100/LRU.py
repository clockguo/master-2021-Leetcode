class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.queun = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.queun.remove(key)
            self.queun.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.queun.remove(key)
        else:
            self.dic[key] = value
            if self.capacity == len(self.queun):
                self.dic.pop(self.queun.pop(0))
        self.queun.append(key)
