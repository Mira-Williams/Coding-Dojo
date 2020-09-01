
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    addFront(value) {
        newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;

        return this;
    }

    removeFront() {
        this.head = this.head.next;

        return this;
    }

    front() {
        if (this.head) {
            return this.head.data;
        }
        return null;
    }

    contains(value) {
        current = this.head

        while(current){
            if (current.data === value){
                return true
            }
            current = current.next
        }
        return false
    }

    length() {
        count = 0
        runner = this.head

        while(runner){
            count ++
            runner = runner.next
        }
        return count
    }

    display() {
        array_vals = []
        runner = this.head

        while(runner){
            array_vals.push(runner.data)
            runner = runner.next
        }

        string_vals = array.join(', ')
        return string_vals
    }

    max() {
        runner = this.head
        max = runner.data;

        while(runner) {
            if (runner.data > max){
                max = runner.data
                runner = runner.next
            }
        }

        return max
    }

    min() {
        runner = this.head
        min = runner.data

        while(runner) {
            if (runner.data < min){
                min = runner.data
                runner = runner.next
            }
        }

        return min
    }

    average() {
        runner = this.head
        sum = 0


        while(runner) {
            sum += runner.data
        }

        ave = sum / this.length()
        return ave
    }
}

