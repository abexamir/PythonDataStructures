class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_at_end(self, new_value):
        new_node = Node(new_value)
        if self.head_node is None:
            self.head_node = new_node
            return
        tail_node = self.head_node
        while tail_node:
            tail_node = tail_node.get_next_node()
        tail_node.set_next_node(new_node)
        
    def insert_after_node(self, prev_node, value):
        if not prev_node:
            print("previous node does not exist")
            return
        new_node = Node(value)
        new_node.set_next_node(prev_node.get_next_node())
        prev_node.set_next_node(new_node)

    def stringify_list(self):
        node = self.get_head_node()
        nodesString = str(node.get_value())
        while node.get_next_node():
            nodesString += "\n" + str(node.get_next_node().value)
            node = node.get_next_node()
        return nodesString

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        while current_node:
            if current_node.get_next_node():
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
            else:
                break
            current_node = current_node.get_next_node()

    def swap_nodes(self, val1, val2):
        print(f'Swapping {val1} with {val2}')

        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            print("Swap not possible - one or more element is not in the list")
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

    def reverse(self):
        prev_node = None
        current_node = self.head_node
        while current_node:
            next_node = current_node.get_next_node()
            current_node.set_next_node(prev_node)
            prev_node = current_node
            current_node = next_node
        self.head_node = prev_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, prev_node):
            if not current_node:
                return prev_node
            next_node = current_node.get_next_node()
            current_node.set_next_node(prev_node)
            prev_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, prev_node)
        self.head_node = _reverse_recursive(current_node=self.get_head_node, prev_node=None)
        
    def get_length(self):
        current_node = self.head_node
        length = 0
        while current_node:
            length = length + 1
            current_node = current_node.get_next_node()
        return length

    def get_length_from_node_to_end(self, node):
        if node is None:
            return 0
        return 1 + self.get_length_from_node_to_end(node.get_next_node())

    def merge_sorted(self, llist):
        p = self.head_node
        q = llist.head_node
        s = None

        if not p:
            return q
        if not q:
            return p 

        if p and q:
            if p.get_value() <= q.get_value():
                s = p 
                p = s.get_next_node()
            else:
                s = q
                q = s.get_next_node()
            new_head = s 
        while p and q:
            if p.get_value() <= q.get_value():
                s.set_next_node(p)
                s = p 
                p = s.get_next_node()
            else:
                s.set_next_node(q)
                s = q
                q = s.get_next_node()
        if not p:
            s.set_next_node(q)
        if not q:
            s.set_next_node(p)

        self.head_node = new_head
        return self.head_node   
    
    def remove_duplicates(self):
        current_node = self.head_node
        prev_node = None
        duplicate_values = dict()

        while current_node:
            if current_node.get_value in duplicate_values:
                prev_node.set_next_node(current_node.get_next_node())
                current_node = None
            else:
                duplicate_values[current_node.get_value()] = 1
                prev_node = current_node
            current_node = prev_node.get_next_node()