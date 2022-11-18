'''
Please use the code template below to complete your assignment.
Your code must go under pa3 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Kevin Nguyen
studentID: 026957825

assignment:PA3
'''
from array import array
import sys

class Solution:
	def pa3 (self, arr: list[int], k: int )	-> int:
     
		arr = [int(i) for i in arr]
		print(arr,k)
  
		#HeapSort algorithm
		def heapify(arr: array, n: int, i: int) -> array:
			l = 2 * i + 1
			r = 2 * i + 2
   
			if (l < n and arr[l] < arr[i]):
				smallest = l
			else:
				smallest = i
    
			if (r < n and arr[r] < arr[smallest]):
				smallest = r
    
			if (smallest != i):
				(arr[i], arr[smallest]) = (arr[smallest], arr[i])
				# (arr[smallest], arr[i]) = (arr[i], arr[smallest])
				heapify(arr, n, smallest)
    
		def build_heap(arr: array) -> array:
			for i in range(int((len(arr) / 2) -1), -1, -1):
				heapify(arr, len(arr), i)
		
		def heapsort(arr: array) -> array:
			build_heap(arr)
   
			for i in range(len(arr) - 1, 0, -1):
				arr[i], arr[0] = arr[0], arr[i]
				heapify(arr, i, 0)

		#kthsmallest algorithm
		def partition(arr: array, p: int, r: int) -> int:
			x = arr[r]
			i = p - 1
			for p in range(p, r):
				if arr[p] <= x:
					i += 1
					(arr[i], arr[p]) = (arr[p], arr[i])
			(arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
			return i + 1

		def kthSmallest(arr: array, l: int, r: int, k: int) -> int:
			if (k > 0 and k <= r - 1):
				q = partition(arr, l, r)
			else:
				q = partition(arr, l, r)
			if (q == k):
				return arr[q]
			elif (q > k):
				return kthSmallest(arr, l, q - 1, k)
			return kthSmallest(arr, q + 1, r, k - q + l)

		heapsort(arr)
		return kthSmallest(arr, 0, len(arr) - 1, k - 1)

    
if __name__ == '__main__':
	arr = sys.argv[1].split(',')
	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)

