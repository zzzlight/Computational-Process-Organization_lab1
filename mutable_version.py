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

    def is_empty(self):
        return self.total_size == 0

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

    def get(self, idx):
        if idx < 0 or idx >= self.total_size:
            return None

        cur = self.head.next
        while idx >= cur.size:
            idx -= cur.size
            cur = cur.next
        return cur.elements[idx]

    def add_to_tail(self, input_obj):
        self.add(self.total_size, input_obj)

    def filter(self, judge):
        result = []
        for i in range(self.total_size):
            if (judge(self.get(i))):
                result.append(i)
        for j in reversed(result):
            self.remove(j)
        return self.to_list()

    def find(self, judge):
        result = []
        for i in range(self.total_size):
            if (not (judge(self.get(i)))):
                result.append(i)
        for j in reversed(result):
            self.remove(j)
        # reversed to keep the idx don't change
        return self.to_list()

    def from_list(self, list, node_size=2):
        if len(list) == 0:
            return
        self.mempty()
        for i in range(len(list)):
            self.add(i, list[i], node_size)

    def to_list(self):
        i = 0
        result = []
        for i in range(self.total_size):
            result.append(self.get(i))
        return result

    def reduce(self, f, initial_state):
        state = initial_state
        for i in range(self.total_size):
            state = f(state, self.get(i))
        return state

    def map(self, f):
        for idx in range(self.total_size):
            cur = self.head.next
            while idx >= cur.size:
                idx -= cur.size
                cur = cur.next
            cur.elements[idx] = f(cur.elements[idx])
        return self

    def mconcat(self, other):
        """
        concat two list to one
        """
        temp = []
        if len(self.to_list()) == 0:
            return other.to_list()
        if len(other.to_list()) == 0:
            return self.to_list()

        temp += self.to_list()
        temp += other.to_list()
        temp.sort()
        result = LinkedList(temp)
        return result.to_list()

    def mempty(self):
        """
            clean the linklist
        """
        if len(self.to_list()) == 0:
            self.total_size = 0
            return self
        i = 0
        for i in range(self.total_size):
            self.remove(i)
        self.total_size = 0
        return self

    def size(self):
        return self.total_size
