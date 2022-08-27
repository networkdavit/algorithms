my_list = [1,5,6,2,3,18,25,27,16]
sorted_list = []

# def sorting(unsorted_list):
# 	list_len = len(unsorted_list) - 1
# 	for i in range(list_len):
# 		temp_list = []
# 		if(unsorted_list[i+1] < unsorted_list[i+2] and unsorted_list[i+1] > unsorted_list[i]):
# 			sorted_list.append(unsorted_list[i])
# 		else:
# 			no_match = unsorted_list.pop(i)
# 			unsorted_list.append(no_match)
# 			# print(no_match)
# 			# print(unsorted_list)
# 	return sorted_list

# print(sorting(my_list))

def bubblesort(list):

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)