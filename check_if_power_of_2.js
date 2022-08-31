// check if a number is a power of 2
// number must be positive
// проверяем, является ли число степенью двойки
// число должно быть положительным

function power_of_two(number) {{
    while(number > 2) {
    number = number/2;
    console.log(number)
  }  
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
  }
}

const power_of_2 = n => n && (n & (n - 1)) === 0;
console.log(power_of_2(64), "asdf")

console.log(power_of_two(64), "vahe");

function solution(positive_int){
    if(positive_int > 0){
        while(true){
            if(positive_int % 2 != 1){
                positive_int = positive_int / 2
                if(positive_int == 1){
                    return true 
                }
            }
            else{
                return false
            }
        }
    }
}

console.log(solution(6))