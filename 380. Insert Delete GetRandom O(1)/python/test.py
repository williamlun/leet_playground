import random


class RandomizedSet:

    def __init__(self):
        self.data_set = list()
        print(self.data_set)

    def insert(self, val: int) -> bool:
        if val in self.data_set:
            return False
        self.data_set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_set:
            return False
        self.data_set.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_set)


# Your RandomizedSet object will be instantiated and called as such:
# Explanation
randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.remove(2)  # Returns false as 2 does not exist in the set.
randomizedSet.insert(2)  # Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom()  # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1)  # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2)  # 2 was already in the set, so return false.
randomizedSet.getRandom()  # Since 2 is the only number in the set, getRandom() will always return 2.


class RandomizedSet2:

    def __init__(self):
        self.data_set = list()
        print(self.data_set)

    def insert(self, val: int) -> bool:
        if val in self.data_set:
            return False
        self.data_set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_set:
            return False
        self.data_set.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_set)
