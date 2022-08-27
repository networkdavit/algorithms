#check if a number is a power of 2

def is_Power_of_two(positive_int):
        return positive_int > 0 and (positive_int & (positive_int - 1)) == 0

def solution(positive_int):
    if(positive_int > 0):
        while True:
            if(positive_int % 2 != 1):
                positive_int = positive_int // 2
                if(positive_int == 1):
                    return True 
            else:
                return False


print(is_Power_of_two(4))


print(solution(120))