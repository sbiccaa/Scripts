//A function can include the return statement but it does not have to. In the case that the function doesn't have a return statement, when you call it, //the function processes the inner code but the returned value is undefined.

//Example

var sum = 0;
function addSum(num) {
  sum = sum + num;
}
addSum(3); // sum will be modified but returned value is undefined addSum is a function without a return statement. The function will change the global sum variable but the returned value of the function is undefined.

//Understanding Undefined Value returned from a Function
// Setup
var sum = 0;

function addThree() {
  sum = sum + 3;
}

// Only change code below this line
function addFive(){
  sum = sum + 5;
}

// Only change code above this line

addThree();
addFive();
