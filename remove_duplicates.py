#remove duplicates from a list

duplicates_list = [1,5,5,2,3,4,6,8,4,5,8,6,4,2]
no_duplicates = []

def remove_duplicates(arr):
    for i in arr:
        if(i not in no_duplicates):
            no_duplicates.append(i)
    return no_duplicates

print(remove_duplicates(duplicates_list))