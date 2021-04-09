class Node:
    def __init__(self, capacity=2):
        self.elements = [None] * capacity
        self.size = 0  # size
        self.cap = capacity  # node's capacity
        self.next = None


class LinkedList:
    def __init__(self, init_list=[], node_size=2):
        self.total_size = 0  # all obj's count
        self.head, self.tail = Node(-1), Node(-1)  # head,tail iter
        node = Node(node_size)
        self.head.next = node
        node.next = self.tail
        for i in range(len(init_list)):
            self.add(i, init_list[i], node_size)

    def iter_node(self, idx):
        cur = self.head.next
        while idx >= cur.size:
            idx -= cur.size
            cur = cur.next
        return cur

    def add(self, idx, obj, node_size=2):
        if idx < 0 or idx > self.total_size:
            return

        # find the insert node and idx
        cur = self.head.next
        while idx >= cur.size:
            if idx == cur.size:
                break
            idx -= cur.size
            cur = cur.next

        if cur.size == cur.cap:
            # node is full ,create new node
            node = Node(node_size)
            next = cur.next
            cur.next = node
            node.next = next

            # 将插入节点一般元素移至新节点
            move_idx = cur.size // 2
            for i in range(move_idx, cur.size):
                node.elements[i - move_idx] = cur.elements[i]
                cur.elements[i] = None
                cur.size -= 1
                node.size += 1

            # update insert idx
            if idx >= move_idx:
                idx -= move_idx
                cur = node

        # insert obj
        for i in range(cur.size - 1, idx - 1, -1):
            cur.elements[i + 1] = cur.elements[i]
        cur.elements[idx] = obj

        cur.size += 1
        self.total_size += 1

    def remove(self, idx):
        if idx < 0 or idx >= self.total_size:
            return

        # find the remove obj's node and idx
        cur = self.head.next
        while idx >= cur.size - 1:
            if idx == cur.size - 1:
                break
            idx -= cur.size
            cur = cur.next

        # remove obj
        for i in range(idx, cur.size - 1, 1):
            cur.elements[i] = cur.elements[i + 1]
        cur.elements[cur.size - 1] = None
        cur.size -= 1

        if cur.next.cap != -1 and cur.cap >= cur.size + cur.next.size:
            # merge the node
            next = cur.next
            for i in range(0, next.size):
                cur.elements[cur.size + i] = next.elements[i]
            cur.size += next.size
            cur.next = next.next

        self.total_size -= 1


"""
following is function 
"""


def remove(self, idx):
    copy = copy_new(self)
    copy.remove(idx)
    return copy


def to_list(self):
    i = 0
    result = []
    for i in range(self.total_size):
        result.append(get(self, i))
    return result


def from_list(self, list, node_size=2):
    if len(list) == 0:
        return
    clean(self)
    for i in range(len(list)):
        self.add(i, list[i], node_size)
    return self


def add_to_tail(self, input_obj):
    copy = copy_new(self)
    copy.add(copy.total_size, input_obj)
    to_list(copy)
    return copy


# def add_to_tail(self, node_list=[]):
#      if self.root is None:
#          self.root = Node(node_list)
#          self.total_size += len(node_list)
#          self.total_cap += len(node_list)
#          return
#      self.last_node().next = Node(node_list)
#      self.total_size += len(node_list)
#      self.total_cap  += len(node_list)
#      return self


def reduce(self, f, initial_state):
    copy = copy_new(self)
    state = initial_state
    for i in range(copy.total_size):
        state = f(state, get(copy, i))
    return state


def map(self, f):
    copy = copy_new(self)
    for idx in range(copy.total_size):
        cur = copy.head.next
        while idx >= cur.size:
            idx -= cur.size
            cur = cur.next
        cur.elements[idx] = f(cur.elements[idx])
    return copy


def clean(self):
    """
        clean the linklist(mutable)
    """
    if len(to_list(self)) == 0:
        self.total_size = 0
        return self
    i = 0
    for i in range(self.total_size):
        self.remove(i)
    self.total_size = 0
    return self


def mconcat(self, other):
    """
    concat two list to one
    """
    copy1 = copy_new(self)
    copy2 = copy_new(other)
    temp = []
    if len(to_list(copy1)) == 0:
        return to_list(copy2)
    if len(to_list(copy2)) == 0:
        return to_list(copy1)

    temp += to_list(copy1)
    temp += to_list(copy2)
    temp.sort()
    result = LinkedList(temp)
    return to_list(result)


def mempty(self):
    """
        clean the linklist
    """
    temp = copy_new(self)
    if len(to_list(temp)) == 0:
        temp.total_size = 0
        return temp
    i = 0
    for i in range(temp.total_size):
        temp.remove(i)
    temp.total_size = 0
    return temp


def cons(self, idx, obj):
    copy = copy_new(self)
    copy.add(idx, obj)
    return copy


def copy_new(self):
    """
    Copy a Linklist ,what cons to do is add on "add" function
    """
    data = to_list(self)
    lst = LinkedList()
    from_list(lst, data)
    return lst


"""
following def don't change the linklist so is the same with version of mutable
"""


def size(self):
    return self.total_size


def is_empty(self):
    return self.total_size == 0


def filter(self, judge):
    copy = copy_new(self)
    result = []
    for i in range(copy.total_size):
        if (judge(get(copy, i))):
            result.append(i)
    for j in reversed(result):
        copy.remove(j)
    return to_list(copy)


def get(self, idx):
    if idx < 0 or idx >= self.total_size:
        return None

    cur = self.head.next
    while idx >= cur.size:
        idx -= cur.size
        cur = cur.next
    return cur.elements[idx]


def find(self, judge):
    copy = copy_new(self)
    result = []
    for i in range(copy.total_size):
        if (not (judge(get(copy, i)))):
            result.append(i)
    for j in reversed(result):
        copy.remove(j)
    # reversed to keep the idx don't change
    return to_list(copy)
