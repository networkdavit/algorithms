# You have a function which should take an array of N length and a number K
# The function should return matrix (array inside an array) with first K elements
# grouped inside the first nested array, next K elements inside the next, etc
# Example:
# test_array = [1,4,5,6,7,2,3,4,6,5,8]
# K = 3
# output = [[1,4,5],[6,7,2],[3,4,6], [5,8]]

test_array = [1,4,5,6,7,2,3,4,6,5,8]
K = 3

def solution(arr, num):
	remainder = len(test_array)%num
	count = 0
	matrix_count = num
	output_array = []
	temp_arr = []
	for i in arr:
		temp_arr.append(i)
		count +=1
		if(count == matrix_count ):
			output_array.append(temp_arr)
			matrix_count = matrix_count + num
			temp_arr = []
	output_array.append(arr[-remainder:])
	return output_array

print(solution(test_array, K))


