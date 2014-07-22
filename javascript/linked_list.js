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
    console.log(itemString, expected);
    return itemString === expected;
  }

  return {
    visit: visit,
    hasResult: hasResult
  };
}

describe('Linked List', function() {

  it('creating a list', function() {
    var visitor = new StringVisitor();
    var first = new Node('A');
    var second = new Node('B');
    first.setNext(second);
    var third = new Node('C');
    second.setNext(third);
    first.accept(visitor);
    assert.ok(visitor.hasResult('ABC'));
  });

});
