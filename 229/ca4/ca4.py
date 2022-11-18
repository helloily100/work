# %% [markdown]
# # CECS 229 Coding Assignment #4 - Answer Key
# 
# #### Due Date: 
# 
# Sunday, 3/20 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the following by the due date:
# 
# 1. **To the BB Dropbox Folder:** this completed .ipynb file
# 
# 2. **To CodePost:** this file converted to a Python script named `ca4.py`
# 
# #### Objectives:
# 
# 1. Apply vector operations to translate, scale, and rotate a set of points representing an image.
# 2. Perform various operations with or on vectors: addition, subtraction, dot product, norm.
# 
# 
# --------------------------------------------------------
# 
# #### Needed Import Statements

# %%
# MAKE SURE TO RUN THIS CELL BEFORE RUNNING ANY TESTER CELLS
import math


# %% [markdown]
# #### Problem 1:
# 
# Create a function `translate(S, z0)` that translates the points in the input set $S$ by $z_0 = a_0 + b_0 i$.  The function should satisfy the following:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `z0` - complex number
# 2. OUT:
#     * `T` - set T consisting of points in S translated by $z_0$

# %%
def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * T - set consisting of points in S translated by z0
    """
    S = S
    t = set()
    for i in S:
        t.add(i+z0)
    return t    


# %% [markdown]
# ------------
# 
# #### Problem 2:
# 
# Create a function `scale(S, k)` that scales the points in the input set $S$ by a factor of $k$:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `k` - positive float, if negative or zero factor is given then the function raises a ValueError with message, "ERROR: Scaling factor must be a positive float".
# 2. OUT:
#     * `T` - set T consisting of points in S scaled by $k$ and rotated by $\theta$

# %%
def scale(S, k):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    S = S
    t = set()
    for i in S:
        t.add(i*k)
    return t


# %% [markdown]
# -----------------------------------
# 
# #### Problem 3:
# 
# Create a function `rotate(S, theta)` that rotates the points in the input set $S$ by $\theta$ radians:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `theta` - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
# 2. OUT:
#     * `T` - set T consisting of points in S rotated by $\theta$

# %%
def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * T - set consisting of points in S rotated by theta radians
        
    """
    S = S
    t = set()
    if theta != 0:
        for i in S:
            n =  i * (2.718281828 ** (theta * 1j))
            t.add(n)
    if theta == 0:
        for i in S:
            t.add(i)
    return t


# %% [markdown]
# --------------------
# #### Problem 4:
# 
# Finish the implementation of class `Vec` which instantiates row-vector objects with defined operations of addition, subtraction, scalar multiplication, and dot product.  In addition, `Vec` class overloads the Python built-in function `abs()` so that when it is called on a `Vec` object, it returns the Euclidean norm of the vector.
# 
# 
# 

# %%
class Vec:
    def __init__(self, contents = []):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        a = math.sqrt(sum(i ** 2 for i in self.elements))
        return a
        
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
        add = []
        for i in range(len(self.elements)):
            add.append(int(self.elements[i] + other.elements[i]))
        return Vec(add)

    
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
        sub = []
        for i in range(len(self.elements)):
            sub.append(self.elements[i] - other.elements[i])
        return Vec(sub)
    
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            #FIXME: IMPLEMENT
            if len(self.elements) != len(other.elements):
                raise ValueError()
            dp = []
            total = 0
            for i in range(len(self.elements)):
                if type(other) == float:
                    dp.append(self.elements[i] * other.elements[i])
                else: 
                    dp.append(int(self.elements[i] * other.elements[i]))
            for i in range(len(dp)):
                total += dp[i]
            return total
            
            
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            scalar = []
            for i in range(len(self.elements)):
                if type(other) == float:
                    scalar.append(self.elements[i] * other)
                else: 
                    scalar.append(int(self.elements[i] * other))
            return Vec(scalar)
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        scalar = []
        for i in range(len(self.elements)):
            if type(other) == float:
                scalar.append(self.elements[i] * other)
            else: 
                scalar.append(int(self.elements[i] * other))
        return Vec(scalar)
    

    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation
