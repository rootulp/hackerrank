'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the repeatedString function below.
function repeatedString(string, numberOfCharactersToConsider) {
    if (string.length > numberOfCharactersToConsider) {
        return countOccurencesOfA(string.substring(0, numberOfCharactersToConsider));
    } else {
        const occurencesOfAInString = countOccurencesOfA(string);
        const numTimesToRepeatString =  timesToRepeatString(string.length, numberOfCharactersToConsider)
        const remainderLength = remainder(string.length, numberOfCharactersToConsider)
        const occurencesOfAInRemainder = countOccurencesOfA(string.substring(0, remainderLength))
        return (occurencesOfAInString * numTimesToRepeatString) + occurencesOfAInRemainder;
    }
}

function countOccurencesOfA(string) {
    return (string.match(/a/g) || []).length;
}

function timesToRepeatString(stringLength, numberOfCharactersToConsider) {
    return Math.floor(numberOfCharactersToConsider / stringLength)
}

function remainder(substringLength, numberOfCharactersToConsider) {
    return numberOfCharactersToConsider % substringLength
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const n = parseInt(readLine(), 10);

    let result = repeatedString(s, n);

    ws.write(result + "\n");

    ws.end();
}
