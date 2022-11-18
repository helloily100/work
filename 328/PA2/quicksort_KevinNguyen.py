'''
name1: Kevin Nguyen

assignment:PA2
'''
from array import array
import sys
import random
import time

class Solution:
	
	#This function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	#This function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count + 1):
			output.append(i)
		return output

	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0,elements_count+1):
			output.append(random.randint(1,1000000000))

		return output


	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if 	input_type == "b":
			output = self.function_b(elements_count)
		if 	input_type == "c":
			output = self.function_c(elements_count, seed)
		return output	

	

	def pa2_quicksort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		
    	# your quicksort algorithm comes here ...
		def partition(arr: array, p: int, r: int):
			x = arr[r]
			i = p - 1
			for p in range(p, r):
				if arr[p] >= x:
					i += 1
					(arr[i], arr[p]) = (arr[p], arr[i])
			(arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
			return i + 1

		def quickSort(arr: array, p: int, r: int):
			if p < r:
				q = partition(arr, p, r)
				quickSort(arr, p, q - 1)
				quickSort(arr, q + 1, r)

		quickSort(query_list, 0, n - 1)
    	# end of quicksort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]


if __name__ == '__main__':
	sys.setrecursionlimit(1500)
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]
	
	obj = Solution()
	ret = obj.pa2_quicksort(input_type, elements_count, seed)
	print(ret)

