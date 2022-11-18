'''
Please use the code template below to complete your assignment.
Your code must go under pa1 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Kevin Nguyen	
studentID: 026957825

assignment:PA1
'''
from cmath import nan
from operator import index
import sys
from tkinter import END

class Solution:
	def pa1 (self, s: str )	-> bool:
		pair = {"(" : ")", "[" : "]", "{" : "}"}
  
  		# base condition
		if (len(s) % 2) != 0:
			return False
		elif not s:
			return 
		for i in s:
			if i not in pair:
				return False
			j = pair[i]
			newS = s[s.index(i)+1:]
			if j in newS:
				s = s.replace(i,"")
				s = s.replace(j,"")
				if not s:
					return True
			else:
				return False

	
				
        
			

if __name__ == '__main__':
	s = sys.argv[1]
	obj = Solution()
	ret = obj.pa1(s)
	print(ret)

