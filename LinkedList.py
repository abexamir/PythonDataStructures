# We'll be using our Node class
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


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Add your insert_beginning and stringify_list methods below:
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

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


# if __name__ == '__main__':
#     ll = LinkedList(5)
#     ll.insert_beginning(6)
#     ll.insert_beginning(8)
#     ll.insert_beginning(7)
#     ll.insert_beginning(5)
#     ll.insert_beginning(8)
#     print(ll.stringify_list())
#     print("-------------------")
#     ll.remove_node(8)
#     print(ll.stringify_list())
#     print("-------------------")
#     ll.remove_node(5)
#     print(ll.stringify_list())
