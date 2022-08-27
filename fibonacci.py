#Fibonacci numbers

def fibonacci(number):
    n1 = 0
    n2 = 1
    next_num = 0

    for i in range(11):
        print(n1)
        next_num = n1+n2
        n1 = n2
        n2 = next_num

fibonacci(11)

