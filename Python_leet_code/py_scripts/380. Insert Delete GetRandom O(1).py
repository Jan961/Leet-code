import random


class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.container_array = []



    def insert(self, val: int) -> bool:
        self.container_array.append(val)
        self.container[val] = len(self.container_array)-1

    def remove(self, val: int) -> bool:
        if self.container.get(val) is None:
            return False

        id = self.container.pop(val)
        self.container_array[id] = self.container_array[-1]
        self.container[self.container_array[id]] = id
        self.container_array.pop()
        return True


    def getRandom(self) -> int:
        return random.choice(self.container_array)


