class Node:
    def __init__(self, node_list=[], next_node=None):
        self.elements = node_list
        self.next = next_node
        self.cap =len(node_list)

        """
        cap single node capacity  size single insert number
        total_size ->use to count  total_cap max-capacity of linklist
        """

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

    def is_empty(self):
        return self.total_size == 0

    def add_to_head(self, node_list=[]):
        node = Node(node_list, self.root)
        self.root = node
        self.total_size += len(node_list)
        self.total_cap  += len(node_list)

    def last_node(self):
        cur = self.root
        while cur.next is not None:
            cur = cur.next
        return cur

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


    def add(self, idx, obj):
        if idx < 0 or idx >= self.total_cap:
            return -1

        # find the location
        cur = self.root

        while idx >= cur.cap:
            if idx == cur.cap:
                idx -= cur.cap
                break
            idx -= cur.cap
            cur = cur.next
        if cur.elements[idx] is None:
            self.total_size += 1
        cur.elements[idx] = obj


    def remove_by_index(self, idx):
        if idx < 0 or idx >= self.total_cap:
            return -1

        cur = self.root
        # find the del node loca
        while idx >= cur.cap:
            if idx == cur.cap:
                idx-=cur.cap
                break
            idx -= cur.cap
            cur = cur.next
        cur.elements[idx] = None
        self.total_size -= 1

    def remove_by_val(self, val):
        cur = self.root
        while (cur is not None):
            for i in range(cur.cap):
                if ((cur.elements[i] is not None) and cur.elements[i]==val):
                    cur.elements[i] = None
                    self.total_size -= 1
                   # cur.size -= 1
            cur = cur.next_node()

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

    def reduce(self, f, initial_state):
        state = initial_state
        cur = self.root
        while (cur is not None):
            for i in range(cur.cap):
                if (cur.elements[i] is not None):
                    state = f(state, cur.elements[i])
            cur = cur.next_node()
        return state

    def map(self, f):
        cur = self.root
        while (cur is not None):
          for i in range(cur.cap):
             if (cur.elements[i] is not None):
                   cur.elements[i]=f(cur.elements[i])
          cur = cur.next_node()


    def mconcat(self, other):
        """
        concat two list to one
        """
        if self.total_size==0 :
            return other
        if other.total_size>0 :
            current = other.root
            record = []
            while current is not None:
                record += current.elements
                current = current.next
            self.add_to_tail(record)
        return self

    def mempty(self):
        """
            clean the linklist
        """
        cur = self.root
        while (cur is not None):
            for i in range(cur.cap):
                if (cur.elements[i] is not None):
                    cur.elements[i] = None
            cur = cur.next_node()
        self.total_size = 0
        return self

    def size(self):
        return  self.total_size