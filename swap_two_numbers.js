//swap 2 numbers without making a temporary variable

function swap(a, b){
  b = b -a;
  a = a+ b;
  b = a-b;
  result = `${a} and ${b}`
  return result
}

console.log(swap(10,26))

