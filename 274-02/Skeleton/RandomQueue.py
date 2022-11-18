import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()


    def add(self, x : object):
        """
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        """
        if self.queue.n + 1 > len(self.queue.a):
            self.queue.resize()
        self.queue.add(x)
        self.queue.a = self.queue.a + 1
        return True


    def remove(self) -> object:
        """
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline
                    decides which element should be removed.
            Return: Object type
        """
        if self.queue.size() == 0: raise IndexError()
        y = self.queue.remove()
        self.queue.n = self.queue.n - 1
        return y
    def size(self) -> int:
        return self.queue.size()


