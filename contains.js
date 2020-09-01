
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

        return this.head;
    }

    removeFront() {
        this.head = this.head.next;

        return this.head;
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

    back(){
        runner = this.head

        while(runner){
            runner = runner.next
        }

        return runner.data
    }

    rem_back(){
        runner = this.head

        while(runner.next.next){
            runner = runner.next
        }

        runner.next = null
        return this.head
    }

    add_back(data){
        runner = this.head

        while(runner){
            runner = runner.next
        }

        runner.next = new Node(data)

        return this.head
    }

    sec_to_last(){
        runner = this.head

        if(this.length() < 3){
            return runner.data
        }

        while(runner.next.next){
            runner = runner.next
        }

        return runner.data
    }

    rem_self(value){
        runner = this.head

        while(runner){
            if(runner.next.data === value){
                runner.next = runner.next.next
                return this.head
            }
            runner = runner.next
        }
    }

    copy(){
        runner = this.head
        newSSL = new SSL()

        while(runner){
            newSSL.addFront(runner.data)
            runner = runner.next
        }

        return newSSL.head
    }

    filter(low, high){
        runner = this.head
        if(runner.data < low || runner.data > high){
            this.head = runner.next
        }

        while(runner){
            if(runner.next.data < low || runner.next.data > high){
                runner.next = runner.next.next
            }
        }

        return this.head
    }
}


// function ListNode(value) {
//     this.val = value;
//     this.next = null;
// }