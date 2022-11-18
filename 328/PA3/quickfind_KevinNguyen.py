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
  
    	# your quicksort algorithm comes here ...
		
		def partition(arr: array, p: int, r: int) -> int:
			x = arr[r]
			i = p - 1
			for j in range(p, r):
				if arr[j] <= x:
					i += 1
					(arr[i], arr[j]) = (arr[j], arr[i])
			(arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
			return i + 1

		def quickSort(arr: array, p: int, r: int) -> array:
			if p < r:
				q = partition(arr, p, r)
				quickSort(arr, p, q - 1)
				quickSort(arr, q + 1, r)

		def kthSmallest(arr: array, l: int, r: int, k: int) -> int:
			if (k > 0 and k <= r - 1):
				q = partition(arr, l, r)
			else:
				q = partition(arr, l, r)

			if (q == k):
				return arr[q]
			if (q > k):
				return kthSmallest(arr, l, q - 1, k)
			return kthSmallest(arr, q + 1, r, k - q + l)

		quickSort(arr, 0, len(arr) - 1)
		return kthSmallest(arr, 0, len(arr) - 1, k - 1)
	
  
if __name__ == '__main__':
	arr = sys.argv[1].split(',')
	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)

