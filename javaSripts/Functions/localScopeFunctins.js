//In JavaScript, scope refers to the visibility of variables. Variables which are defined outside of a function block have Global scope. This means, they can be seen everywhere in your JavaScript code.

//Variables which are used without the var keyword are automatically created in the global scope. //Variables which are declared within a function, as well as the function parameters have local scope. That means, //they are only visible within that function.


//Local Scope and Functions


function myLocalScope() {

var myVar = 10;
  // Only change code below this line

  console.log('inside myLocalScope', myVar);
}
myLocalScope();

console.log(myVar)

// Run and check the console
// myVar is not defined outside of myLocalScope


