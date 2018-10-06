import unittest
from load import load_strings


def linear_search(element, items: list, verbose: bool=False) -> int:

    for index, item in enumerate(items):

        if verbose:
            print(index)

        if element == item:
            return index

    raise ValueError('Element not found')


def binary_search(element, items: list, verbose: bool=False) -> int:

    first = 0
    last = len(items) - 1

    while first < last:

        midpoint = (first + last) // 2

        if element == items[midpoint]:
            return midpoint
        elif element < items[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

        if verbose:
            print(first, midpoint, last)

    raise ValueError('Element not found')


class SearchSpec(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.unsorted_names = load_strings('names/unsorted.txt')
        cls.sorted_names = load_strings('names/sorted.txt')

    def test_linear_search(self):
        self.assertEqual(linear_search('Keva Camren', self.unsorted_names), 53675)

    def test_linear_search_not_found(self):
        with self.assertRaises(ValueError):
            linear_search('John Doe', self.unsorted_names)

    def test_binary_search(self):
        self.assertEqual(binary_search('Keva Camren', self.sorted_names), 55984)

    def test_binary_search_not_found(self):
        with self.assertRaises(ValueError):
            binary_search('John Doe', self.sorted_names)


if __name__ == '__main__':
    unittest.main()
