from mutable_version import *
import unittest
from hypothesis import given
import hypothesis.strategies as st

"""
folloing function is used in map and reduce
"""


def judge(num):
    return num % 2 == 0


def fun(x, y):
    return x + y


class TestMutableList(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_mutable(self, a):
        test_list1 = LinkedList([1, 2, None, 4, 5, 6])
        test_list2 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8], 4)
        # set single node capacity as 4 not default 2
        test_list3 = LinkedList(a)
        self.assertEqual(test_list1.to_list(), [1, 2, None, 4, 5, 6])
        self.assertEqual(test_list2.to_list(), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(test_list3.to_list(), a)

    """
     these code shows that the function mutable and can change by function
    """

    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        test_data = [
            [],
            ['a'],
            ['a', 'b', 'c']
        ]
        lst = LinkedList([])
        for e in iter(test_data):
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

        testlist1 = LinkedList()
        testlist1.from_list(a)
        self.assertEqual(testlist1.to_list(), a)

    @given(st.lists(st.integers()))
    def test_to_list(self, a):
        testlist1 = LinkedList(['a', 2, 'b', 3, 5, 6])
        self.assertEqual(testlist1.to_list(), ['a', 2, 'b', 3, 5, 6])
        testlist2 = LinkedList(a)
        self.assertEqual(testlist2.to_list(), a)

    @given(st.lists(st.integers()))
    def test_size(self, b):
        test_list1 = LinkedList(b)
        test_list2 = LinkedList(['a'])
        test_list3 = LinkedList([])
        self.assertEqual(test_list3.size(), 0)
        self.assertEqual(test_list1.size(), len(b))
        self.assertEqual(test_list2.size(), 1)

    # find not even
    def test_find(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(test_list1.find(judge), [2, 4, 6])

    def test_add(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        test_list1.add(3, 22)
        self.assertEqual(test_list1.to_list(), [1, 2, 4, 22, 3, 5, 6])

    # filter and what left is even
    def test_filter(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(test_list1.filter(judge), [1, 3, 5])

    def test_map(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        result = test_list1.map(lambda x: x + 2)
        self.assertEqual(result.to_list(), [3, 4, 6, 5, 7, 8])

    def test_reduce(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(test_list1.reduce(fun, 0), 21)

    @given(st.lists(st.integers()))
    def test_mempty(self, a):
        x = [1, 2, 4, 3, 7, 5, 6]
        test_list1 = LinkedList(x)
        result1 = test_list1.mempty()
        test_list2 = LinkedList(a)
        result2 = test_list2.mempty()
        self.assertEqual(result1.to_list(), [])
        self.assertEqual(result1.size(), 0)
        self.assertEqual(result2.size(), 0)

    # remove by index
    def test_remove(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        test_list1.remove(2)
        self.assertEqual(test_list1.to_list(), [1, 2, 3, 5, 6])

    @given(st.lists(st.integers()))
    def test_mconcat(self, a):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        test_list2 = LinkedList()
        test_list3 = LinkedList([1, 2, 4, 'a', 'b'])
        test_list4 = LinkedList(a)
        self.assertEqual(test_list1.mconcat(test_list2), [1, 2, 4, 3, 5, 6])
        self.assertEqual(test_list3.mconcat(test_list2), [1, 2, 4, 'a', 'b'])
        self.assertEqual(test_list4.mconcat(test_list2), a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_monoid_identity(self, a, b):
        testlist_a = LinkedList(a)
        testlist_b = LinkedList(b)
        self.assertEqual(testlist_a.mconcat(testlist_b), testlist_b.mconcat(testlist_a))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        testlist_a = LinkedList(a)
        testlist_b = LinkedList(b)
        testlist_c = LinkedList(c)
        a_b = testlist_a.mconcat(testlist_b)
        b_a = testlist_b.mconcat(testlist_a)
        self.assertEqual(a_b, b_a)
        c_b = testlist_c.mconcat(testlist_b)
        b_c = testlist_b.mconcat(testlist_c)
        self.assertEqual(c_b, b_c)
        a_b__c = testlist_c.mconcat(LinkedList(a_b))
        a__b_c = testlist_a.mconcat(LinkedList(b_c))
        self.assertEqual(a_b__c, a__b_c)

    def test_add_to_tail(self):
        test_list2 = LinkedList([1, 2, 4, 3, 5, 6])
        test_list2.add_to_tail('x')
        self.assertEqual(test_list2.to_list(), [1, 2, 4, 3, 5, 6, 'x'])


if __name__ == '__main__':
    unittest.main()
