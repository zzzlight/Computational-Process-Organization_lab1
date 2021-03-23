from unmutable_version import *
import unittest
from hypothesis import given
import hypothesis.strategies as st

"""
folloing function is used in map and reduce
"""
def judge(num):
    if num % 2 ==0:
        return  True
    return  False

def fun(x, y) :
    return x + y

class TestMutableList(unittest.TestCase):

     def test_unmutable(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(remove_by_val(test_list1, 2).to_list(), [[1, None, 4, 3], [5], [6]])
         self.assertEqual(test_list1.to_list(),[[1, 2, 4, 3], [5], [6]])
         """
          these code shows that the function just remove on the copy of original list,but the original is unmutable and not change
         """

     def test_from_list(self):
         test_data = [
             [],
             ['a'],
             ['a', 'b']
         ]
         for e in test_data:
             lst = LinkedList(Node(e))
             lst.from_list(e)
             self.assertEqual(lst.to_list_test(), e)

     def test_add(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         result=add(test_list1,3, 22)
         self.assertEqual(result.to_list(), [[1, 2, 4, 22], [5], [6]])

     def test_to_list(self):
         a = Node(['a', 2, 'b', 3], Node([5], Node([6])))
         testlist1=LinkedList(a)
         self.assertEqual(testlist1.to_list(),[['a',2,'b',3],[5],[6]])

     def test_size(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1=LinkedList(a)
         test_list2=LinkedList(Node(['a']))
         self.assertEqual(size(None), 0)
         self.assertEqual(size(test_list1), 6)
         self.assertEqual(size(test_list2),1)

     def test_find(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(find(test_list1,judge),[2,4,6])


     def test_filter(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(find(test_list1,judge),[2,4,6])


     def test_map(self):
           a = Node([1, 2, 4, 3], Node([5], Node([6])))
           test_list1 = LinkedList(a)
           self.assertEqual(map(test_list1,lambda x: x + 2).to_list(), [[3, 4, 6, 5], [7], [8]])


     def test_reduce(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(reduce(test_list1, fun, 0),21)

     def test_mempty(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(mempty(test_list1).to_list(),[[None, None, None, None], [None], [None]])
         self.assertEqual(size(mempty(test_list1)), 0)
         self.assertEqual(test_list1.to_list(), [[1,2,4,3],[5],[6]])


     def test_remove_by_val(self):
            a = Node([1, 2, 4, 3], Node([5], Node([6])))
            test_list1 = LinkedList(a)
            self.assertEqual(remove_by_val(test_list1,2).to_list(), [[1,None,4,3],[5],[6]])

     def test_remove_by_index(self):
            a = Node([1, 2, 4, 3], Node([5], Node([6])))
            test_list1 = LinkedList(a)
            self.assertEqual(remove_by_index(test_list1,2).to_list(), [[1,2,None,3],[5],[6]])


     def test_mconcat(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         test_list2=LinkedList(None)
         test_list3=LinkedList(Node([1, 2, 4, 'a'],Node(['b'])))
         self.assertEqual(mconcat(test_list1, test_list2).to_list(),[[1, 2, 4, 3], [5], [6]])
         self.assertEqual(mconcat(test_list3,test_list1).to_list(),[[1, 2, 4, 'a'], ['b'], [1, 2, 4, 3, 5, 6]])
         self.assertEqual(mconcat(test_list3, test_list2).to_list(),[[1, 2, 4, 'a'], ['b']])

     def test_add_to_tail(self):
         a = Node([1, 2, 4, 3], Node([5], Node([6])))
         test_list1 = LinkedList(a)
         self.assertEqual(add_to_tail(test_list1,['x']).to_list(),[[1, 2, 4, 3], [5], [6], ['x']])



if __name__ == '__main__':
    unittest.main()

