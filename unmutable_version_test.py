from unmutable_version import *
import unittest
from hypothesis import given
import hypothesis.strategies as st

def judge(num):
    if num % 2 ==0:
        return  True
    return  False
def fun(x, y) :
    return x + y

class TestMutableList(unittest.TestCase):

    # def test_from_list(self):
    #     test_data = [
    #         [],
    #         ['a'],
    #         ['a', 'b']
    #     ]
    #
    #     for e in test_data:
    #         lst = UnrolledLinkedList(Node(e))
    #         lst.from_list(e)
    #         self.assertEqual(lst.to_list(), e)

    def test_size(self):
        a = Node([1,2,4,3], Node([5], Node([6])))
        # b = Node([333])
        test_list = LinkedList(a)
       # print(test_list.to_list())
       #  other_list=LinkedList(b)
       # # print(test_list.to_list())
       #  test_list.add(5,14)
        # test_list.remove_by_val(2)
        # test_list.remove_by_index(5)
        # x=to_list(test_list)
        # print(x)
        # x=cons(test_list)
        # print(x.to_list())
        print(mempty(test_list).to_list())
        print(test_list.to_list())
        # print(to_list(y))
        # print(size(test_list))
        # print(reduce(test_list,fun,0))
        # test_list.map(lambda x: x + 2)
        # print(test_list.to_list())
     #   print(test_list.to_list())
        # test_list.insert(1,3)
        #test_list.add(1, 'a')

        #print(test_list.total_size)

        #print(test_list.total_cap)

        #print(list)
        #print(test_list.size())
        #print(test_list.find(judge))
        #print(test_list.filter(judge))
        #//test_list.mconcat(other_list)
        #//print(test_list.to_list())
        #test_list.filter_is_even()
        #print(test_list.size())

        # self.assertEqual(test_list.total_size, )
        # test_list.add_to_tail(30)
        # test_list.insert(21, 'a')
        # self.assertEqual(UnrolledLinkedList(Node()).size(), 2)
        # self.assertEqual(test_list.total_size, 1)
        #
        # b = test_list.iter_node()
        # # # #
        # while(b is not None):
        #     for i in range(b.cap):
        #      print(b.elements[i])
        #     b = b.next_node()


if __name__ == '__main__':
    unittest.main()



