'''
name1: Kevin Nguyen

assignment:PA2
'''
import math
from array import array
from heapq import merge
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

	

	def pa2_mergesort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		
    	# your merge sort algorithm comes here ...
		def merge(arr, left, mid, right):
			n1 = mid - left + 1
			n2 = right - mid
			L = [0] * n1
			R = [0] * n2
   
			for i in range(0, n1):
				L[i] = arr[left + i]
			
			for j in range(0, n2):
				R[j] = arr[mid + j + 1]

			L.append(math.inf * -1)
			R.append(math.inf * -1)

			i = j = 0
			k = left

			for k in range(left, right + 1):
				if L[i] >= R[j]:
					arr[k] = L[i]
					i += 1
				else:
					arr[k] = R[j]
					j += 1


		def mergeSort(arr, left, right):
			if left < right:
				mid = (left + right) // 2
    
				mergeSort(arr, left, mid)
				mergeSort(arr, mid + 1, right)
				merge(arr, left, mid, right)
    
		mergeSort(query_list, 0, n - 1)
		# end of merge sort
			
		et = time.process_time()
		res = et - st

		return [query_list, res]

	


if __name__ == '__main__':
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]
	
	obj = Solution()
	ret = obj.pa2_mergesort(input_type, elements_count, seed)
	print(ret)

