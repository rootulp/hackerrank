'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'fizzBuzz' function below.
 *
 * The function accepts INTEGER n as parameter.
 */
function fizzBuzz(n) {
    for (var i = 1; i <= n; i++) {
        if (i % 5 == 0 && i % 3 == 0) {
            console.log("FizzBuzz");
        } else if (i % 5 == 0) {
            console.log("Buzz")
        } else if (i % 3 == 0) {
            console.log("Fizz")
        } else {
            console.log(i)
        }
    }
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    fizzBuzz(n);
}
