//If you'll recall from our discussion of Storing Values with the Assignment Operator, everything to the right of the equal sign is resolved before the value is assigned. This means we can take the return value of a function and assign it to a variable.

//Assume we have pre-defined a function sum which adds two numbers together, then:

ourSum = sum(5, 12);

//will call sum function, which returns a value of 17 and assigns it to ourSum variable.

// Setup
var changed = 0;

function change(num) {
  return (num + 3) / 5;
}

// Only change code below this line
changed = change(10);

var processed = 0;

function processArg(num){
  return (num + 3) / 5;


processed = processArg(7);
