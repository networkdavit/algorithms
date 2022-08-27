my_list = [5, 6, -25, -7,3, 1, 2, 9, 15, 4]
my_list.sort()
import time

# get the start time


for i in range(len(my_list)):
    st = time.time()
    if(my_list[i] > 0):
        solution = my_list[i]+1
        if(solution != my_list[i + 1]):
            et = time.time()

            elapsed_time = et - st
            print('Execution time:', elapsed_time, 'seconds')
            print(f"{solution} is the solution")
            break
            

my_list2 = [5, 6, -25, -7,3, 1, 2, 9, 15, 4]
def solution(any_list):
    st = time.time()
    list_len = len(any_list)
    N = set(range(1, list_len + 2))
    et = time.time()

    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return min(N-set(any_list))

test = solution(my_list2)
print(test)
