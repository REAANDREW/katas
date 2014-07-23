var assert = require('assert');

function Node(item) {

  var first;
  var last;
  var next;

  
  function setNext(node) {
    next = node;
    if(first === null || first === undefined){
      node.setFirst(self);
    }else{
      node.setFirst(first);
    }
    var nodeFirst = node.getFirst();
    nodeFirst.setLast(node);
    setLast(node);
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

  function setFirst(node){
    first = node;
  }

  function getFirst(){
    return first;
  }

  function accept(visitor) {
    visitor.visit(item)
    if (next !== undefined && next !== null) {
      next.accept(visitor);
    }
  }

  var self = Object.freeze({
      item: item,
      setNext: setNext,
      getNext: getNext,
      getLast: getLast,
      setLast: setLast,
      setFirst : setFirst,
      getFirst : getFirst,
      accept: accept
  });

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
    assert.equal(first.getLast(), undefined);
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

  it('the second item can report the last item in a three node linked list', function(){
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

  it('setting the last node updates the first node so that it reflects the new last node', function(){
    var oldLast = chain.getLast();
    var last = new Node('Z');
    oldLast.setNext(last);
    chain.setLast(last);
    var newLast = chain.getLast();
    assert.equal(newLast.item, 'Z');
  });



});
