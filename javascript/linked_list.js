var assert = require('assert');

function Node(item) {

  var next;

  function setNext(node) {
    next = node;
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

  function createChain(){
    var first = new Node('A');
    var second = new Node('B');
    first.setNext(second);
    var third = new Node('C');
    second.setNext(third);
    return first;
  }

  it('creating a list', function() {
    var visitor = new StringVisitor();
    var chain = createChain();
    chain.accept(visitor);
    assert.ok(visitor.hasResult('ABC'));
  });

  it('insert at the beginning', function(){
    var visitor = new StringVisitor();
    var chain = createChain();
    var oldFirst = chain;
    var first = new Node('Z');
    first.setNext(oldFirst);
    first.accept(visitor);
    assert.ok(visitor.hasResult('ZABC'));
  });

});
