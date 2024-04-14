import random


class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.hashMap
        if res:
            self.hashMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            index = self.hashMap[val]
            lastVal = self.numList[-1]
            self.numList[index] = lastVal
            self.numList.pop()
            self.hashMap[lastVal] = index
            del self.hashMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Instantiate RandomizedSet
random_set = RandomizedSet()

# Insert elements
print(random_set.insert(1))  # Output: True
print(random_set.insert(2))  # Output: True
print(random_set.insert(3))  # Output: True
print(random_set.insert(4))  # Output: True
print(random_set.insert(2))  # Output: False (2 is already in the set)

# Get a random element
print(random_set.getRandom())  # Output: Random element from the set

# Remove elements
print(random_set.remove(3))  # Output: True (3 is removed from the set)
print(random_set.remove(5))  # Output: False (5 is not in the set)

# Get a random element after removal
print(random_set.getRandom())  # Output: Random element from the updated set
