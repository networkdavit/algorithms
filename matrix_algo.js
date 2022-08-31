// You have a function which should take an array of N length and a number K
// The function should return matrix (array inside an array) with first K elements
// grouped inside the first nested array, next K elements inside the next, etc
// Example:
// test_array = [1,4,5,6,7,2,3,4,6,5,8]
// K = 3
// output = [[1,4,5],[6,7,2],[3,4,6], [5,8]]

let test_array = [1,4,5,6,7,2,3,4,6,5,8]
let K = 3

function solution(arr, num){
	let remainder = test_array.length%num
	let count = 0
	let matrix_count = num
	let output_array = []
	let temp_arr = []
	for (i in arr){
		temp_arr.push(arr[i])
		count +=1
		if(count == matrix_count ){
			output_array.push(temp_arr)
			matrix_count = matrix_count + num
			temp_arr = []
		}
	}
	output_array.push(arr.slice(-remainder))
	return output_array
}
console.log(solution(test_array, K))
