//When a condition for an if statement is true, the block of code following it is executed. What about when that condition is false? Normally nothing would happen. //With an else statement, an alternate block of code can be executed.

if (num > 10) {
  return "Bigger than 10";
} else {
  return "10 or Less";
}
//Combine the if statements into a single if/else statement.

function testElse(val) {
  var result = "";
  // Only change code below this line

  if (val > 4 && val >= 6) {
    result = "Bigger than 5";
  } else {
    result = "5 or Smaller";
  }

  // Only change code above this line
  return result;
}

testElse(4);

//work in progress 


var count = 0;

function cc(card) {
  // Only change code below this line

var holdbet = 'hold'
var bet = 'bet'
if (count => 2 && count <= 6){
 return count + " " + bet;
} else 
if (count => 7 && count <= 9){
  return 'bet'+ card
} else
if (count => 7 && count <= 9){
  return 'hold'+ card
}
return count + " " + holdbet;
  // Only chang code above this line
}

cc(2); cc(3); cc('k'); cc(10); cc('A');
console.log(cc('2'))



