var assert = require('assert');

function Node(item) {

    var first = null;
    var last = null;
    var next = null;
    var previous = null;

    function setNext(node) {
        if (node === null || node === undefined) {
            next = node;
            return;
        }
        next = node;
        node.setFirst(first);
        node.setPrevious(self);
        var nodeFirst = node.getFirst();
        nodeFirst.setLast(node);
        setLast(node);
    }

    function getPrevious() {
        return previous;
    }

    function setPrevious(node) {
        previous = node;
    }

    function getNext() {
        return next;
    }

    function setLast(node) {
        last = node;
    }

    function getLast() {
        return last;
    }

    function setFirst(node) {
        first = node;
    }

    function getFirst() {
        return first;
    }

    function pop() {
        var firstItem = self.getFirst();
        var last = firstItem.getLast();
        var previous = last.getPrevious();
        previous.setNext(null);
        firstItem.setLast(previous);
        return last;
    }

    function push(node){
        var firstItem = self.getFirst();
        var oldLast = firstItem.getLast();
        oldLast.setNext(node);
        first.setLast(node);
    }

    function unshift(node){
        var oldFirst = self.getFirst();
        node.setNext(self);
        return node;
    }

    function accept(visitor) {
        visitor.visit(item)
            if (next !== undefined && next !== null) {
                next.accept(visitor);
            }
    }

    var self = {
        item: item,
        getPrevious: getPrevious,
        setPrevious: setPrevious,
        setNext: setNext,
        getNext: getNext,
        getLast: getLast,
        setLast: setLast,
        setFirst: setFirst,
        getFirst: getFirst,
        pop: pop,
        push : push,
        unshift : unshift,
        accept: accept
    };
    first = last = self;

    return self;
}

function StringVisitor() {
    var itemString = '';

    function visit(nodeItem) {
        itemString += nodeItem;
    }

    function assertResult(expected) {
        assert.equal(itemString, expected);
    }

    return {
        visit: visit,
            assertResult: assertResult
    };
}

describe('Linked List', function() {

    var visitor;
    var chain;

    beforeEach(function() {
        visitor = new StringVisitor();
        chain = createChain();
    });

    function createChain() {
        var first = new Node('A');
        var second = new Node('B');
        first.setNext(second);
        var third = new Node('C');
        second.setNext(third);
        return first;
    }

    it('creating a list', function() {
        chain.accept(visitor);
        visitor.assertResult('ABC');
    });

    it('insert at the beginning', function() {
        var oldFirst = chain;
        var first = new Node('Z');
        first.setNext(oldFirst);
        first.accept(visitor);
        visitor.assertResult('ZABC');
    });

    it('remove item from the beginning', function() {
        var first = chain.getNext();
        first.accept(visitor);
        visitor.assertResult('BC');
    });

    it('sets the last node with one node', function() {
        var first = new Node('A');
        assert.equal(first.getLast(), first);
    });

    it('sets the last node when the next node is set', function() {
        var first = new Node('A');
        var second = new Node('B');
        first.setNext(second);
        assert.equal(first.getLast().item, 'B');
    });

    it('sets the last node when a linked list is created with three nodes', function() {
        var first = new Node('A');
        var second = new Node('B');
        var third = new Node('C');
        first.setNext(second);
        second.setNext(third);
        assert.equal(first.getLast().item, 'C');
    });

    it('the second item can report the last item in a three node linked list', function() {
        var second = chain.getNext();
        var last = second.getLast();
        assert.equal(last.item, 'C');
    });

    it('adds an item to the end', function() {
        var oldLast = chain.getLast();
        var last = new Node('Z');
        oldLast.setNext(last);
        chain.setLast(last);
        chain.accept(visitor);
        visitor.assertResult('ABCZ');
    });

    it('setting the last node updates the first node so that it reflects the new last node', function() {
        var oldLast = chain.getLast();
        var last = new Node('Z');
        oldLast.setNext(last);
        chain.setLast(last);
        var newLast = chain.getLast();
        assert.equal(newLast.item, 'Z');
    });

    it('supports popping the last node', function() {
        var oldLast = chain.pop();
        assert.equal(oldLast.item, 'C');
        assert.equal(chain.getLast().item, 'B');
    });

    it('supports pushing an item onto the end', function() {
        var a = new Node('A');
        var b = new Node('B');
        a.push(b);
    });

    it('supports unshifting an item on to the beginning and returning the new beginning node', function(){
        var a = new Node('A');
        a= a.unshift(new Node('B'));
        assert.equal(a.item, 'B');
    });

    it('supports shifting an item from the beginning', function(){

    });

    it.skip('speed of a native array', function() {

        var a = [];
        for (var i = 0; i < 100000; i++) {
            a.push(new Node(i));
        }
        while (a.length > 0) {
            a.pop();
        }

    });

    it.skip('speed of a linked list', function() {
        var a = new Node('A');

        for (var i = 0; i < 100000; i++) {
            a.push(new Node(i));
        }

        while(a.getNext() != null){
            var item = a.pop();
        }

    });

});
