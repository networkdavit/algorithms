// You have a function which will get 3 inputs, total amount of water in grams, how much water 
// has already been spilled per minute shown in an array(array of integers), and how many seconds have passed
// If the water hasn't been completely spilled, estimate the rate at which the remaining water
// will be spilled
// Write a function:
// function solution(x,y,z), where x is the total water, y is the array of k length with integers of how much was spilled
// z is the time passed
// Example:
// x = 100, y = [10,6,6,8], z = 2
// x = total amount in grams
// y = first second spilled 8, second 6, third, 6, fourth, 10
// z = how many seconds have passed
// 30 grams of water was spilled (10+6+6+8)
// 70 grams remain (100-30)
// The average of the last 2 minutes is 7(6+8)/2
// Your function should return 10 (70/7)

// У вас есть функция, которая получит 3 входа, общее количество воды в граммах, сколько воды
// уже было пролито за минуту показанное в массиве (массив целых чисел), и сколько секунд прошло
// Если вода не была полностью пролита, оцените скорость, с которой оставшаяся вода
// будет пролит
// Напишите функцию:
// function solution(x,y,z), где x — общее количество воды, y — массив длины k с целыми числами того, сколько воды было пролито
// z - время, прошедшее
// Пример:
// х = 100, у = [10,6,6,8], г = 2
// x = общее количество в граммах
// y = первая вторая пролитая 8, вторая 6, третья, 6, четвертая, 10
// z = сколько секунд прошло
// Пролито 30 грамм воды (10+6+6+8)
// Осталось 70 грамм (100-30)
// Среднее значение за последние 2 минуты равно 7(6+8)/2.
// Ваша функция должна вернуть 10 (70/7)

//David
function solution(x,y,z){
    if(z > 0){
        let total_downloaded = 0
        for(let i in y){
            total_downloaded = total_downloaded + y[i]
        }
        const remaining = x - total_downloaded
        const last_z_mins = y.slice(-z)
        let sum_of_z_mins = 0

        for(i in last_z_mins){
            sum_of_z_mins = sum_of_z_mins + last_z_mins[i]
        }
        
        const average_of_last_minutes = sum_of_z_mins/z
        return Math.ceil(remaining/average_of_last_minutes)
    }
    else{
        return -1
    }
}

console.log(solution(100, [10,6,6,8], 2))
console.log(solution(10, [2,3], 2))


//Nikola
function calc(x, y, z){
    let last_z_mins = y.slice(-z)
    const average = last_z_mins.reduce((partialSum, a) => partialSum + a, 0)/2; 
    const sum = y.reduce((partialSum, a) => partialSum + a, 0);   
    const remainder = x - sum
    return Math.ceil(remainder/average)
}

console.log(calc(100, [10,6,6,8], 2))
console.log(calc(10, [2,3], 2))

//Write a function, which takes 2 numbers as an argument and returns them
//in reverse order
//Example:
//function swap(7,10) should return 10 7

//Напишем функцию, которая принимает 2 числа в качестве аргумента и возвращает их
//в обратном порядке
//Пример:
//function swap(7,10) должна возвращать 10 7
