# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, node):
        self.next = node

    def add(self, node):
        # carry
        sum = self.val + node.val
        if sum >= 10:
            if self.next:
                self.next.val += 1
            else:
                self.next = ListNode(1)
        self.val = sum % 10

        if self.next:
            self.next.add(node.next)

    def print(self):
        print(self.val, end='')
        if self.next:
            print('->', end='')
            self.next.print()
        else:
            print()


def merge_two_list(list1, list2):
    pass

def create_list_from_arry(arr):
    root = ListNode(arr[0])
    current = root
    for val in arr[1:]:
        node = ListNode(val)
        current.append(node)
        current = node
    return root

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

l1 = create_list_from_arry([2,4,3])
l2 = create_list_from_arry([5,6,4])
l1.add(l2)
l1.print()

class TwoSumTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_addTwoNumbers(self):
        l1 = create_list_from_arry([2,4,3])
        l1.print()
        print('test')