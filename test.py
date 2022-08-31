def power_of_two(number):
    while(number > 2):
        number = number/2;
        
    
    if (number % 2 == 0):
        return True;
    else:
        return False;
   

print(power_of_two(64), "vahe");
