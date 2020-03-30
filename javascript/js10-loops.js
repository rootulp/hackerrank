'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(string) {
    for(const char of string) {
        if (isVowel(char)) {
            console.log(char)
        }
    }
    for(const char of string) {
        if (isConsonant(char)) {
            console.log(char)
        }
    }
}

function isVowel(char) {
    return char === "a" || char === "e" || char === "i" || char === "o" || char === "u"
}

function isConsonant(char) {
    return !isVowel(char)
}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
