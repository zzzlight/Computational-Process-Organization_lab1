from mutable_version import *
import unittest
from hypothesis import given
import hypothesis.strategies as st

"""
folloing function is used in map and reduce
"""
def judge(num):
    if num % 2 == 0:
        return True
    return False


def fun(x, y):
    return x + y


class TestMutableList(unittest.TestCase):


    def test_mutable(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)
        test_list1.remove_by_val(1)
        result = test_list1.remove_by_val(2)
        self.assertEqual(result.to_list(), [[None, None, 4, 3], [5], [6]])

    """
     these code shows that the function mutable and can change by function
    """

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b', 'c']
        ]
        for e in test_data:
            lst = LinkedList(Node(e))
            lst.from_list(e)
            self.assertEqual(lst.to_list_test(), e)

    def test_to_list(self):
        a = Node(['a', 2, 'b', 3], Node([5], Node([6])))
        testlist1 = LinkedList(a)
        self.assertEqual(testlist1.to_list(), [['a', 2, 'b', 3], [5], [6]])

    @given(st.lists(st.integers()))
    def test_size(self,b):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(Node(b))
        test_list2 = LinkedList(Node(['a']))
        test_list3 = LinkedList(Node())
        self.assertEqual(test_list3.size(), 0)
        self.assertEqual(test_list1.size(), len(b))
        self.assertEqual(test_list2.size(), 1)

    def test_find(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)

        self.assertEqual(test_list1.find(judge), [2, 4, 6])

    def test_add(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1=LinkedList(a)
        test_list1.add(3,22)
        self.assertEqual(test_list1.to_list(),[[1, 2, 4, 22], [5], [6]] )



    def test_filter(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)
        self.assertEqual(test_list1.find(judge), [2, 4, 6])

    def test_map(self):
        b = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(b)
        result = test_list1.map(lambda x: x + 2)
        self.assertEqual(result.to_list(), [[3, 4, 6, 5], [7], [8]])

    def test_reduce(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)
        self.assertEqual(test_list1.reduce(fun, 0), 21)

    @given(st.lists(st.integers()))
    def test_mempty(self,a):
        x = Node([1, 2, 4, 3, 7], Node([5], Node([6])))
        test_list1 = LinkedList(x)
        result1 = test_list1.mempty()
        test_list2=LinkedList(Node(a))
        result2=test_list2.mempty()
        self.assertEqual(result1.to_list(), [[None, None, None, None, None], [None], [None]])
        self.assertEqual(result1.size(), 0)
        self.assertEqual(result2.size(), 0)

    def test_remove_by_val(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)
        test_list1.remove_by_val(2)
        result = test_list1.remove_by_val(2)
        self.assertEqual(result.to_list(), [[1, None, 4, 3], [5], [6]])

    def test_remove_by_index(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list1 = LinkedList(a)
        test_list1.remove_by_index(2)
        self.assertEqual(test_list1.to_list(), [[1, 2, None, 3], [5], [6]])

    def test_mconcat(self):
        test_list1 = LinkedList(Node([1, 2, 4, 3], Node([5], Node([6]))))
        test_list2 = LinkedList(None)
        test_list3 = LinkedList(Node([1, 2, 4, 'a'], Node(['b'])))
        self.assertEqual(test_list1.mconcat(test_list2).to_list(),[[1, 2, 4, 3], [5], [6]])
        self.assertEqual(test_list3.mconcat(test_list2).to_list(),[[1, 2, 4, 'a'], ['b']])


    def test_add_to_tail(self):
        a = Node([1, 2, 4, 3], Node([5], Node([6])))
        test_list2 = LinkedList(a)
        test_list1 = LinkedList(Node(['x']))
        test_list2.add_to_tail(['x'])
        self.assertEqual(test_list2.to_list(), [[1, 2, 4, 3], [5], [6], ['x']])


if __name__ == '__main__':
    unittest.main()
