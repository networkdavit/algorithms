#Binary search

binary_array = [5,7,12, 17, 25, 31, 32, 37, 45, 59, 61, 78]
number = 25

def search(sorted_list, key):
    min_num = 0
    max_num = len(sorted_list) - 1
    while min_num < max_num:
        mid_num = round((min_num + max_num)/2)
        
        if sorted_list[mid_num] == key:
           return mid_num
        elif sorted_list[mid_num] < key:
             min_num = mid_num + 1
        else: 
            max_num = mid_num -1
    return -1


result = search(binary_array, number)
print(result)

