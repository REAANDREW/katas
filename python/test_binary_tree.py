import unittest


class BinaryTree:

  def __init__(self, number):
    self.number = number
    self.leftChild = None
    self.rightChild = None

  def add(self, number):
    if number < self.number:
      if self.leftChild is None:
        self.leftChild = BinaryTree(number)
      else:
        self.leftChild.add(number)
    else:
      if self.rightChild is None:
        self.rightChild = BinaryTree(number)
      else:
        self.rightChild.add(number)

  def __str__(self):
    leftChildString = ''
    rightChildString = ''
    if self.leftChild is not None:
      leftChildString = str(self.leftChild)
    if self.rightChild is not None:
      rightChildString = str(self.rightChild)
    return str("{0}[{1},{2}]".format(
        self.number, leftChildString, rightChildString))


class TestBinaryTree(unittest.TestCase):

  def testCreatingANewBinaryTree(self):
    tree = BinaryTree(1)
    self.assertEquals("1[,]", str(tree))

  def testAddingLesserNumberGoesToTheLeft(self):
    tree = BinaryTree(2)
    tree.add(1)
    self.assertEquals("2[1[,],]", str(tree))

  def testAddingGreaterNumberGoesToTheRight(self):
    tree = BinaryTree(2)
    tree.add(3)
    self.assertEquals("2[,3[,]]", str(tree))

  def testAddingTwoLevelsOfChildren(self):
    tree = BinaryTree(4)
    tree.add(3)
    tree.add(2)
    self.assertEquals("4[3[2[,],],]", str(tree))


class TestBinaryTreeWithStrings(unittest.TestCase):

  def testCreatingANewBinaryTree(self):
    tree = BinaryTree("P")
    tree.add("Q")
    tree.add("C")
    tree.add("A")
    tree.add("B")
    self.assertEquals("P[C[A[,B[,]],],Q[,]]", str(tree))


# class TestConvertingBinaryTreeIntoBreathFirstView(unittest.TestCase):

   # def testConvertingShallowTree(self):
   #    pass
   #    """
   #    1st child = i*2+1
   #    2nd child = i*2+2
   #         _______
   #        |_____  |
   #        |     | |
   #    0|1|2|3|4|5|6
   #      |___| |
   #      |_____|
   #    """
   #    tree = BinaryTree(6)
   #    tree.add(5)
   #    tree.add(7)
   #    tree.add(4)
   #    tree.add(3)
   #    tree.add(2)
   #    breathFirstVisitor = BreadthFirstVisitor()
   #    tree.accept(breathFirstVisitor)


class TestBalancingABinarySearchTree(unittest.TestCase):

  def testARightRotation(self):
    pass


if __name__ == "__main__":
  unittest.main()
