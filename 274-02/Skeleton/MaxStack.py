from Interfaces import Stack
import SLLStack


class MaxStack(Stack):
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        self.max = SLLStack.SLLStack()

    def max(self) -> object:
        '''
            Returns the max element
        '''
        if self.size() != 0:
            return self.max.head.x
        else:
            raise IndexError()

    def push(self, x: object):
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        tail = x
        if (self.max.size() != 0 and tail < self.max.head.x):
            tail = self.max.head.x
            self.max.push(tail)

        if self.stack.size() == 0:
            self.push(tail)
        else:
            self.push(self.stack.head.x)
            self.stack.tail.x = tail






    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        if self.size() == 0:
            raise IndexError()

        self.max.pop()
        return self.stack.pop()

    def size(self) -> int:
        return self.stack.size()


