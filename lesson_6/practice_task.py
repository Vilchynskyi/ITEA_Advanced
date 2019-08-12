class MyList:

    __slots__ = '_my_list', '_size'

    def __init__(self, some_list):
        self._my_list = some_list
        self._size = len(self._my_list)

    def __getitem__(self, idx):
        if idx > self._size - 1:
            raise StopIteration('Out of range')
        return self._my_list[idx]

    def __str__(self):
        return str(self._my_list)

    def pop(self, idx):
        if idx < len(self._my_list):
            self._my_list = self._my_list[:idx] + self._my_list[1 + idx:]
        else:
            raise IndexError('pop index out of range')

    def append(self, item):
        self._my_list = self._my_list + [item]

    def insert(self, idx, item):
        self._my_list = self._my_list[:idx] + [item] + self._my_list[idx:]

    def remove(self, item):
        if item in self._my_list:
            for i in range(len(self._my_list) - 1):
                if self._my_list[i] == item:
                    del self._my_list[i]
        else:
            raise ValueError('list.remove(x): x not in list')

    def clear(self):
        self._my_list = []

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self._my_list + other.get_list())
        else:
            raise TypeError('can add list to list only')

    def get_list(self):
        return self._my_list


first_list = MyList([45, 78, 30])
print(first_list[0])
first_list.pop(0)
first_list.append('str')
first_list.insert(2, 2675)
first_list.remove(78)
print(first_list)

second_list = MyList([12, 34, 454])

print(first_list + second_list)


class MyDict:

    __slots__ = '_my_dict'

    def __init__(self, some_dict):
        self._my_dict = some_dict

    def __str__(self):
        return str(self._my_dict)

    def get(self, item):
        try:
            return self._my_dict[item]
        except KeyError:
            return

    def items(self):
        return self._my_dict

    def keys(self):
        keys = []
        for i in self._my_dict:
            keys.append(i)
        return keys

    def values(self):
        keys = MyDict.keys(self)
        values = []
        for i in keys:
            values.append(self._my_dict[i])
        return values

    def __add__(self, other):
        if isinstance(other, MyDict):
            temp_dict = self._my_dict
            temp_dict.update(other.get_dict())
            return MyDict(temp_dict)
        else:
            raise TypeError('can add dict to dict only')

    def get_dict(self):
        return self._my_dict


first_dict = MyDict({1: 2, 3: 4, 5: 6})
print(first_dict.get(1))
print(first_dict.items())
print(first_dict.keys())
print(first_dict.values())

second_dict = MyDict({11: 22, 33: 44, 55: 66})
print(first_dict + second_dict)
