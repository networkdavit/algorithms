nums = [1,5,6,12,65, 123, 590, 621, 789]
number = 590

def binary_search(arr, num)
	min = 0
	max = arr.length() - 1
	while min <= max 
		mid = (min + max)/2.floor()
		if arr[mid] == num
			return mid
		elsif arr[mid] < num
			min = mid + 1
		else
			max = mid - 1
		end
	end
end

puts binary_search(nums, number)