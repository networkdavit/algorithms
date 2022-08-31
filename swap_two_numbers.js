//swap 2 numbers without making a temporary variable

function swap(a, b){
  b = b -a;
  a = a+ b;
  b = a-b;
  return `${a} and ${b}`
}

console.log(swap(10,26))

function swap1(a, b) {
  a = a+b;
  b=a-b;
  a=a-b;
  
  console.log("a is " + a + "and b is " +b)
}

swap1(5,6);

function swap3(a,b){
  a = a + b;//5+6=11
  b = a - b;//11-6=5
  a = a - b;//11-5=6
  return console.log(a, b) ;
}
swap3(5,6)