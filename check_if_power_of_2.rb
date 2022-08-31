#check if a number is a power of 2

def solution (positive_int)
    if positive_int > 0
        while true
            if positive_int % 2 != 1
                positive_int = positive_int / 2
                if positive_int == 1
                    return true 
                end
            else
                return false
            end
        end
     end
end


puts(solution(64))