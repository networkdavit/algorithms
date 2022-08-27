//find_missing_number

let my_array = [1,2,3,4,5,6,7,8,10];
function findMissingNum (arr){
  for(let i = 0; i < arr.length - 1; i++) {
    if(arr[i] + 1 != arr[i+1] ) {
      return arr[i] + 1;
    }
  }
  
  return false;
}

console.log(findMissingNum(my_array))
