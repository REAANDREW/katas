var assert = require('assert');

function Node(item) {

  var next;

  function setNext(node) {
    next = node;
  }

  function getNext(){
    return next;
  }

  function accept(visitor) {
    visitor.visit(item)
    if (next !== undefined && next !== null) {
      next.accept(visitor);
    }
  }

  return {
    item: item,
    setNext: setNext,
    getNext : getNext,
    accept: accept
  };

}

function StringVisitor() {

  var itemString = '';

  function visit(nodeItem) {
    itemString += nodeItem;
  }

  function hasResult(expected) {
    return itemString === expected;
  }

  return {
    visit: visit,
    hasResult: hasResult
  };
}

describe('Linked List', function() {

  var visitor;
  var chain;

  beforeEach(function(){
    visitor = new StringVisitor();
    chain = createChain();
  });

  function createChain(){
    var first = new Node('A');
    var second = new Node('B');
    first.setNext(second);
    var third = new Node('C');
    second.setNext(third);
    return first;
  }

  it('creating a list', function() {
    chain.accept(visitor);
    assert.ok(visitor.hasResult('ABC'));
  });

  it('insert at the beginning', function(){
    var oldFirst = chain;
    var first = new Node('Z');
    first.setNext(oldFirst);
    first.accept(visitor);
    assert.ok(visitor.hasResult('ZABC'));
  });

  it('remove item from the beginning',function(){
    var first = chain.getNext();
    first.accept(visitor);
    assert.ok(visitor.hasResult('BC'));
  });

});
