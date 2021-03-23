class Node:
    def __init__(self, node_list=[], next_node=None):
        self.elements = node_list
        self.next = next_node
        self.cap =len(node_list)   #cap 单节点固定容量  size当前节点插入容量
                                #total_size作用同count计数  total_cap 链表总容量

    def next_node(self):
        if self is None:
            return None
        return self.next


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.total_size = 0
        current=root
        while current is not None:
            self.total_size += current.cap
            current = current.next
        self.total_cap =self.total_size

    def iter_node(self):
        return self.root

    def from_list(self,list=[[]]):
        if(list==[[]]):
            return
        temp=self.root
        for i in range (len(list)) :
            print(list[i])
            temp=Node(list[i])
            temp=temp.next

    def to_list(self):
        current = self.root
        result = []
        while current is not None:
            record = []
            record += current.elements
            result.append(record)
            current = current.next
        return result

    def last_node(self):
        cur = self.root
        while cur.next is not None:
            cur = cur.next
        return cur



"""
following is function 
"""

def add_to_head(self, node_list=[]):
    copy=cons(self)
    node = Node(node_list, copy.root)
    copy.root = node
    copy.total_size += len(node_list)
    copy.total_cap  += len(node_list)



def add_to_tail(self, node_list=[]):
     if self.root is None:
         print(node_list)
         self.root = Node(node_list)

         self.total_size += len(node_list)
         self.total_cap += len(node_list)
         return
     self.last_node().next = Node(node_list)
     self.total_size += len(node_list)
     self.total_cap  += len(node_list)


def remove_by_index(self, idx):
     copy=cons(self)
     if idx < 0 or idx >= self.total_cap:
         return -1

     cur = copy.root
    # the same with version mutable
     while idx >= cur.cap:
         if idx == cur.cap:
             idx-=cur.cap
             break
         idx -= cur.cap
         cur = cur.next
     cur.elements[idx] = None
     copy.total_size -= 1
     return copy

def remove_by_val(self, val):
    copy = cons(self)
    cur = copy.root
    while (cur is not None):
        for i in range(cur.cap):
            if ((cur.elements[i] is not None) and cur.elements[i]==val):
                cur.elements[i] = None
                copy.total_size -= 1
        cur = cur.next_node()
    return copy


def reduce(self, f, initial_state):
    state = initial_state
    copy=cons(self)
    cur = copy.root
    while (cur is not None):
        for i in range(cur.cap):
            if (cur.elements[i] is not None):
                state = f(state, cur.elements[i])
        cur = cur.next_node()
    return state


def map(self, f):
    copy=cons(self)
    cur = copy.root
    while (cur is not None):
      for i in range(cur.cap):
         if (cur.elements[i] is not None):
               cur.elements[i]=f(cur.elements[i])
      cur = cur.next_node()
    return  copy


def mconcat(self, other):
    """
    concat two list to one
    """
    copy_self=cons(self)
    copy_other=cons(other)
    if copy_self.total_size==0 :
        return copy_other
    if copy_other.total_size>0 :
        current = copy_other.root
        record = []
        while current is not None:
            record += current.elements
            current = current.next
        copy_self.add_to_tail(record)
    return copy_self

def mempty(self):
    copy=cons(self)
    cur = copy.root
    while (cur is not None):
        for i in range(cur.cap):
            if (cur.elements[i] is not None):
                cur.elements[i] = None
        cur = cur.next_node()
    copy.total_size = 0
    return copy

def cons(self) :
    """
    Copy a Linklist
    """
    data=self.to_list()
    a=Node(data)
    lst=LinkedList(a)
    # lst.from_list(data)
    return lst


"""
following def don't change the linklist so is the same with version of mutable
"""
def size(self) :
    return  self.total_size

def is_empty(self):
    return self.total_size == 0

def filter(self,judge):
    result=[]
    cur = self.root
    while (cur is not None):
        for i in range(cur.cap):
            if (cur.elements[i] is not None) and (not judge(cur.elements[i])):
                result.append(cur.elements[i])
        cur = cur.next_node()
    return  result

def get(self, idx):
    if idx < 0 or idx >= self.total_cap:
        return None

    cur = self.root
    while idx >= cur.cap:
        if idx == cur.cap:
            break
        idx -= cur.cap
        cur = cur.next
    return cur.elements[idx]

def find(self,judge):
    result=[]
    cur = self.root
    while(cur is not None):
      for i in range(cur.cap):
        if (cur.elements[i] is not None) and (judge(cur.elements[i])):
            result.append(cur.elements[i])
      cur = cur.next_node()
    return  result




