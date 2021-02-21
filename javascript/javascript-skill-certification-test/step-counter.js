class FixedCounter {
    constructor(k) {
        this.counter = counter
        this.k = k
    }

    increment() {
        this.counter.changeBy(this.k)
    }

    decrement() {
        this.counter.changeBy(-this.k)
    }

    getValue() {
        return this.counter.getValue()
    }
}

function getFixedCounter(k) {
    return new FixedCounter(k);
}
