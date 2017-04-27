import unittest


def insertion_sort(array):
  for i in range(0, len(array)):
    for j in range(len(array) - 1, i, -1):
      if array[j] < array[j - 1]:
        swap = array[j - 1]
        array[j - 1] = array[j]
        array[j] = swap
  return array


def insertion_sort_2(array):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = key

  return array


def reverse_insertion_sort(array):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] < key:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = key

  return array


class InsertionSortTest(unittest.TestCase):

  def test_insertion_sort(self):
    input = [4, 1, 5, 8, 2, 3, 6, 9, 7, 10]
    output = insertion_sort(input)
    self.assertEquals(output, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

  def test_insertion_sort_2(self):
    input = [4, 1, 5, 8, 2, 3, 6, 9, 7, 10]
    output = insertion_sort_2(input)
    self.assertEquals(output, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

  def test_reverse_insertion_sort(self):
    input = [4, 1, 5, 8, 2, 3, 6, 9, 7, 10]
    output = reverse_insertion_sort(input)
    self.assertEquals(output, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
  unittest.main()
