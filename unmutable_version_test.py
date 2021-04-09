from unmutable_version import *
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

    def test_unmutable(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        result = cons(test_list1, 3, 22)
        self.assertEqual(to_list(result), [1, 2, 4, 22, 3, 5, 6])
        self.assertEqual(to_list(test_list1), [1, 2, 4, 3, 5, 6])
        test_list2 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8], 4)
        # set single node capacity as 4 not default 2
        """
         these code shows that the function just remove on the copy of original list,but the original is unmutable and not change
        """

    @given(st.lists(st.integers()))
    def test_from_list(self, a):
        test_data = [
            [],
            ['a'],
            ['a', 'b', 'c']
        ]
        lst = LinkedList()
        for e in iter(test_data):
            from_list(lst, e)
            self.assertEqual(to_list(lst), e)

        test_list1 = LinkedList()
        from_list(test_list1, a)
        self.assertEqual(to_list(test_list1), a)

    def test_cons(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        result = cons(test_list1, 3, 22)
        self.assertEqual(to_list(result), [1, 2, 4, 22, 3, 5, 6])

    @given(st.lists(st.integers()))
    def test_to_list(self, a):
        testlist1 = LinkedList(['a', 2, 'b', 3, 5, 6])
        self.assertEqual(to_list(testlist1), ['a', 2, 'b', 3, 5, 6])
        testlist2 = LinkedList(a)
        self.assertEqual(to_list(testlist2), a)

    @given(st.lists(st.integers()))
    def test_size(self, b):
        test_list1 = LinkedList(b)
        test_list2 = LinkedList(['a'])
        test_list3 = LinkedList([])
        self.assertEqual(size(test_list3), 0)
        self.assertEqual(size(test_list1), len(b))
        self.assertEqual(size(test_list2), 1)

    # find not even
    def test_find(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(find(test_list1, judge), [2, 4, 6])

    # filter and what left is even
    def test_filter(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(filter(test_list1, judge), [1, 3, 5])

    def test_map(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        result = map(test_list1, lambda x: x + 2)
        self.assertEqual(to_list(result), [3, 4, 6, 5, 7, 8])

    def test_reduce(self):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        self.assertEqual(reduce(test_list1, fun, 0), 21)

    @given(st.lists(st.integers()))
    def test_mempty(self, a):
        x = [1, 2, 4, 3, 7, 5, 6]
        test_list1 = LinkedList(x)
        result1 = mempty(test_list1)
        test_list2 = LinkedList(a)
        result2 = mempty(test_list2)
        self.assertEqual(to_list(result1), [])
        self.assertEqual(size(result1), 0)
        self.assertEqual(size(result2), 0)

    def test_remove(self):
        test_list1 = LinkedList([1, 2, 4, 3, 7, 5, 6])
        self.assertEqual(to_list(remove(test_list1, 2)), [1, 2, 3, 7, 5, 6])

    @given(st.lists(st.integers()))
    def test_mconcat(self, a):
        test_list1 = LinkedList([1, 2, 4, 3, 5, 6])
        test_list2 = LinkedList()
        test_list3 = LinkedList([1, 2, 4, 'a', 'b'])
        test_list4 = LinkedList(a)
        self.assertEqual(mconcat(test_list1, test_list2), [1, 2, 4, 3, 5, 6])
        self.assertEqual(mconcat(test_list3, test_list2), [1, 2, 4, 'a', 'b'])
        self.assertEqual(mconcat(test_list4, test_list2), a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()))
    def test_monoid_identity(self, a, b):
        testlist_a = LinkedList(a)
        testlist_b = LinkedList(b)
        self.assertEqual(mconcat(testlist_a, testlist_b), mconcat(testlist_b, testlist_a))

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        testlist_a = LinkedList(a)
        testlist_b = LinkedList(b)
        testlist_c = LinkedList(c)
        a_b = mconcat(testlist_a, testlist_b)
        b_a = mconcat(testlist_b, testlist_a)
        self.assertEqual(a_b, b_a)
        c_b = mconcat(testlist_c, testlist_b)
        b_c = mconcat(testlist_b, testlist_c)
        self.assertEqual(c_b, b_c)
        a_b__c = mconcat(testlist_c, LinkedList(a_b))
        a__b_c = mconcat(testlist_a, LinkedList(b_c))
        self.assertEqual(a_b__c, a__b_c)

    def test_add_to_tail(self):
        test_list2 = LinkedList([1, 2, 4, 3, 5, 6])
        result = add_to_tail(test_list2, 'x')
        self.assertEqual(to_list(result), [1, 2, 4, 3, 5, 6, 'x'])


if __name__ == '__main__':
    unittest.main()
