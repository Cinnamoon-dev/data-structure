class Stack {
    constructor(data, next) {
        this.data = data
        this.next = next
    }

    push(value) {
        if(this.data === undefined) {
            this.data = value
            return
        }

        let aux = new Stack(this.data, this.next)
        this.data = value
        this.next = aux
        return
    }

    pushArray(array) {
        array.forEach((e) => {
            this.push(e)
        })
    }

    pop() {
        if(this.data === undefined) {
            return undefined
        }

        if(this.next === undefined) {
            let peak = this.data
            this.data = undefined
            
            return peak
        }

        let peak = this.data

        this.data = this.next.data
        this.next = this.next.next
        return peak
    }

    toArray() {
        let aux = new Stack(this.data, this.next)
        let array = []

        while(aux.data !== undefined) {
            let value = aux.pop()
            array = array.concat(value)
        }

        return array
    }

    peak() {
        return this.data
    }

    print() {
        let aux = new Stack(this.data, this.next)

        while(aux !== undefined) {
            console.log(aux.data)
            aux = aux.next
        }
    }

    isEmpty() {
        return this.data === undefined
    }

    length() {
        if(this.data === undefined) {
            return 0
        }

        let aux = new Stack(this.data, this.next)
        let length = 0

        while(aux !== undefined) {
            length += 1
            aux = aux.next
        }

        return length
    }
}

let stack = new Stack()
stack.pop()

console.log(stack)

// stack.push(2)
// stack.push(3)
// stack.push(4)

// stack.print()

// stack.pushArray([5, 6, 7, 8])
// stack.print()