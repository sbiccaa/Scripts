var count = 0;

function cc(card) {

switch(card) {
case 2:
case 3:
case 4:
case 5:
case 6:
     count++;
     break
case 10:
case 'J':
case 'K':
case 'Q':
case 'A':
      count --;
      break
}

var halbet = 'hoid'
if (count > 0) {
holdbet = 'bet';
}

return count + " " + holdbet;
  

}
cc(2); cc(3); cc('K'); cc(10); cc('A');
console.log(cc('0'))
