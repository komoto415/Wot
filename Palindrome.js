let str = "a  a a";
var isPalinedrome = true;
for (var i = 0; i < (str.length / 2); i++) {
    if (str[0] != str[str.length - 1]) {
        isPalinedrome = false;
        break;
    }
}
console.log(isPalinedrome);