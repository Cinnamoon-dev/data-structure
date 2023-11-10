class Stack { // peak = 0, base = n
    data: any = null
    next: Stack | null = null

    constructor(data: any, next: Stack | null) {
        this.data = data
        this.next = next
    }

    push(data: any) {
        if(data === null) {
            return
        }

        if(this.data === null) {
            this.data = data
            return
        }

        this.next = new Stack(this.data, this.next)
        this.data = data
        return
    }

    pop() {
        if(this.data === null) {
            return null
        }

        if(this.next === null) {
            let data: any = this.data
            this.data = null
            
            return data
        }

        let data: any = this.data

        this.data = this.next.data
        this.next = this.next.next

        return data
    }

    peak() {
        return this.data
    }

    isEmpty() {
        return this.data === null
    }

    length() {
        let aux: Stack = new Stack(this.data, this.next)
        let counter: number = 0;

        while(aux.next !== null) {
            counter = counter + 1
            aux = aux.next
        }

        return counter + 1
    }

    last() {
        let aux: Stack = new Stack(this.data, this.next)

        while(aux.next !== null) {
            aux = aux.next
        }

        return aux.data
    }

    getValueByIndex(index: number) { 
        let aux: Stack = new Stack(this.data, this.next)
        
        for(let i = 0; i < aux.length(); i++) {
            if(i === index) {
                return aux.data
            }

            aux = aux.next
        }

        return null
    }

    getIndexByValue(value: any) {
        let aux: Stack = new Stack(this.data, this.next)
        
        for(let i = 0; i < aux.length(); i++) {
            if(aux.data === value) {
                return i
            }

            aux = aux.next
        }

        return null
    }

    getAllIndexesByValue(value: any) {
        let aux: Stack = new Stack(this.data, this.next)
        let indexes: Array<number> = []

        for(let i = 0; i < aux.length(); i++) {
            if(aux.data === value) {
                indexes.push(i)
            }

            aux = aux.next
        }

        return indexes
    }

    getAllValuesByIndexes(indexes: Array<number>) {
        let aux: Stack = new Stack(this.data, this.next)
        let values: Array<any> = []

        for(let i = 0; i < aux.length(); i++) {
            if(i in indexes) {
                values.push(aux.data)
            }

            aux = aux.next
        }

        return values
    }

    getValuesBySlice(begin: number, end: number) {
        let aux: Stack = new Stack(this.data, this.next)
        let values: Array<any> = []

        for(let i = 0; i < aux.length(); i++) {
            if(begin <= i && i <= end) {
                values.push(aux.data)
            }

            aux = aux.next
        }

        return values
    }

    removeAll() {
        this.data = null
        this.next = null
    }

    removeByIndex(index: number) {
        let aux: Stack = new Stack(this.data, this.next)
    }
}
