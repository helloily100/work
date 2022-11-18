import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
        self.e = ""

    def Intro_expression(self, expression :str):
        self.e = expression

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def print_expression(self, s: str) -> str:
        t = ''
        for s1 in s:
            if (self.dict.find(s1) != None):
                s1 = self.dict.find(s1)
            t = t + str(s1)
        return t

    def matched_expression(self, s: str) -> bool:
        expression = ArrayStack.ArrayStack()
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        for i in s:
            if i in open:
                expression.push(i)
            elif i in close:
                pos = close.index(i)
                if expression.size() > 0:
                    expression.pop()
                else:
                    return False
            if len(expression) == 0:
                return True
            else:
                return False

    tree = BinaryTree.BinaryTree()
    stack = ArrayStack.ArrayStack()
    temp = BinaryTree.BinaryTree.Node('')

    def build_parse_tree(self, exp: str) -> str:
        t = BinaryTree.BinaryTree()
        t.r = t.Node('')
        u = t.r
        for token in exp:
            if u == None:
                u = t.Node('')
            if token == '(':
                u.insert_left()
                u = u.left
            elif token in ["+", "-", "/", "*"]:
                u.x = token
                u.insert_right()
                u = u.right
            elif token == ")":
                if u.parent != None:
                    u = u.parent
                else:
                    u.parent = t.Node('')
                    u.parent.left = t.r
                    t.r = u.parent
                    u = u.parent
            elif token == " ":
                pass
            else:
                u.x = token
                u = u.parent
        return t

    def _evaluate(self, u):
        if u == None:
            return 0

        if u.left == None and u.right == None:
            return int(u.data)

        leftsum = self._evaluate(u.left)
        rightsum = self._evaluate(u.right)

        if u.data == '+':
            return leftsum + rightsum
        elif u.data == '-':
            return leftsum - rightsum
        elif u.data == '*':
            return leftsum * rightsum
        else:
            return leftsum / rightsum

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            return 0



