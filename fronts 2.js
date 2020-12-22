
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
}

