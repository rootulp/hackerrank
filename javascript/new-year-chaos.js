'use strict';

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

// Complete the minimumBribes function below.
function minimumBribes(initialState) {
    if (invalid(initialState)) {
        return "Too chaotic"
    }
    return calculateMinimumBribes(initialState)
}

function invalid(initialState) {
    return initialState.some(didPersonBribeMoreThanTwoPeople)
}

function didPersonBribeMoreThanTwoPeople(person, index) {
    // People are 1 indexed so need to subtract one
    return index + 2 < person - 1
}

function calculateMinimumBribes(line) {
    const initialLine = calculateInitialLine(line)
    let currentLine = line.slice()
    let numberOfSwaps = 0;

    while (currentLine.toString() !== initialLine.toString()) {
        // console.log(`currentLine ${currentLine}, initialLine ${initialLine}`)
        swapNextPerson(currentLine)
        numberOfSwaps += 1
    }
    return numberOfSwaps;
}

function calculateInitialLine(line) {
    // Clone line to avoid modifying original line
    let initialLine = line.slice()
    return initialLine.sort()
}

function swapNextPerson(currentLine) {
    const indexToSwap = currentLine.findIndex(isPersonAheadOfNeighbor)
    swapPersonAtIndex(currentLine, indexToSwap);
}

// WARNING: modifies line in place
function swapPersonAtIndex(currentLine, index) {
    var personToSwap = currentLine[index]
    currentLine[index] = currentLine[index + 1]
    currentLine[index + 1] = personToSwap
}

function isPersonAheadOfNeighbor(person, index, line) {
    return person > line[index + 1]
}

function main() {
    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine(), 10);

        const q = readLine().split(' ').map(qTemp => parseInt(qTemp, 10));

        console.log(minimumBribes(q));
    }
}
