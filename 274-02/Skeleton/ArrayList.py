import numpy as np
from Interfaces import List

class ArrayList(List):
    '''
        ArrayList: Implementation of a List interface using Arrays.
    '''
    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j).
        '''
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n : int) ->np.array:
        """
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        """
        return np.zeros(n, object)

    def resize(self):
        """
        resize: Create a new array and copy the old values.
        """
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i : int) -> object:
        """
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        """
        if 0 >= i >= self.n: raise IndexError()
        return self.a[(i + self.j) % len(self.a)]

    def set(self, i : int, x : object) -> object:
        """
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object
        """
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i + self.j) % len(self.a)] = x
        return y

    def append(self, x : object) :
        self.add(self.n, x)

    def add(self, i : int, x : object) :
        '''
            add: shift one position all the items j>=i, insert an element
            at position i of the list and increment the number of elements
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        '''
        print('a:', self.a)
        if self.n == len(self.a):
            self.resize()

        print('i:', i, 'n:', self.n)
        if i < self.n/2:
            self.j = (self.j - 1) % len(self.a)
            print('j:', self.j)
            for k in range(0, i-1):
                print('aa:', (self.j + k) % len(self.a))
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
        else:
            for k in range(self.n, i + 1, -1):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        self.n = self.n + 1

    def remove(self, i : int) -> object:
        x = self.a[(i + self.j) % len(self.a)]
        if i < self.n/2:
            for k in range(i, 0, -1):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-2):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
        self.n = self.n - 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        s += f"] {self.n} : {self.j}"
        return s

    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input:
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator +=1
        else:
             raise StopIteration()
        return x






s = ArrayList()
s.add(0, 4)
s.add(0, 1)
s.add(1, 3)
s.add(1, 2)
s.add(4, 5)
print('s:', s)
s.remove(2)
s.remove(3)
print(s)
