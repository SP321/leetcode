class MyHashSet:
    def __init__(self):
        self.tablesize = int(1e4 * 10 / 7)
        self.hashtable = [[] for _ in range(self.tablesize)]

    def add(self, key: int) -> None:
        bucket = self.hashtable[key % self.tablesize]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.hashtable[key % self.tablesize]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.hashtable[key % self.tablesize]
        return key in bucket

