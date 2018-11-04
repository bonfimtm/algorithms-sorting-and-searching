import random
import unittest
from load import load_numbers


def is_sorted(items: list) -> bool:

    for index in range(len(items) - 1):
        if items[index] > items[index + 1]:
            return False

    return True


def get_index_of_lowest(items: list) -> int:

    index_of_lowest = 0

    for index, item in enumerate(items):
        if item < items[index_of_lowest]:
            index_of_lowest = index

    return index_of_lowest


def bogo_sort(items: list, verbose: bool=False) -> list:

    sorted_items = items.copy()
    attempts = 0

    while not is_sorted(sorted_items):
        random.shuffle(sorted_items)
        attempts += 1

    if verbose:
        print(attempts, 'attempts')

    return sorted_items


def selection_sort(items: list, verbose: bool=False) -> list:

    unsorted_items = items.copy()
    sorted_items = []

    if verbose:
        print('%-25s %-25s' % (unsorted_items, sorted_items))

    while unsorted_items:
        index_lowest = get_index_of_lowest(unsorted_items)
        sorted_items.append(unsorted_items.pop(index_lowest))
        if verbose:
            print('%-25s %-25s' % (unsorted_items, sorted_items))

    return sorted_items


def quick_sort(items: list, verbose: bool=False) -> list:

    if len(items) <= 1:
        return items

    pivot = items[0]
    left = []
    right = []

    for index in range(1, len(items)):
        if items[index] < pivot:
            left.append(items[index])
        else:
            right.append(items[index])

    if verbose:
        print('i %25s %2s %-25s' % (left, pivot, right))

    return quick_sort(left, verbose) + [pivot] + quick_sort(right, verbose)


def merge_sort(items: list, verbose: bool=False) -> list:

    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left = merge_sort(items[:middle_index], verbose)
    right = merge_sort(items[middle_index:], verbose)

    sorted_items = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_items += [left[left_index]]
            left_index += 1
        else:
            sorted_items += [right[right_index]]
            right_index += 1

    if left_index < len(left):
        sorted_items += left[left_index:]

    if right_index < len(right):
        sorted_items += right[right_index:]

    if verbose:
        print('i %-10s' % sorted_items)

    return sorted_items


class SortSpec(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.numbers_5 = load_numbers('numbers/5.txt')
        cls.numbers_8 = load_numbers('numbers/8.txt')
        cls.numbers_10k = load_numbers('numbers/10k.txt')
        cls.numbers_1kk = load_numbers('numbers/1kk.txt')

    def test_bogo_sort(self):

        unsorted_items = self.numbers_5
        print('u', unsorted_items)

        sorted_items = bogo_sort(unsorted_items)
        print('s', sorted_items)

        self.assertTrue(sorted(unsorted_items) == sorted_items)

    def test_selection_sort(self):

        unsorted_items = self.numbers_5
        print('u', unsorted_items)

        sorted_items = selection_sort(unsorted_items)
        print('s', sorted_items)

        self.assertTrue(sorted(unsorted_items) == sorted_items)

    def test_quick_sort(self):

        unsorted_items = self.numbers_10k
        print('u', unsorted_items)

        sorted_items = quick_sort(unsorted_items)
        print('s', sorted_items)

        self.assertTrue(sorted(unsorted_items) == sorted_items)

    def test_merge_sort(self):

        unsorted_items = self.numbers_10k
        print('u', unsorted_items)

        sorted_items = merge_sort(unsorted_items)
        print('s', sorted_items)

        self.assertTrue(sorted(unsorted_items) == sorted_items)


if __name__ == '__main__':
    unittest.main()
