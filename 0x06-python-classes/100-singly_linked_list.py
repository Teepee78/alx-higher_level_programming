#!/usr/bin/python3
"""Creates a singly linked list

Args:
    Node (class): defines a node of a singly linked list
    SinglyLinkedList (class): defines a singly linked list
"""


class Node:
    """Node: node of a singly linked list

    Args:
        data (int): data of node
        next_node (Node): pointer to next node in singly linked list
    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data: data of node

        setter validates data to be an integer

        Raises:
            TypeError: if data is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node: next node in list

        setter validates next_node is None or a node

        Raises:
            TypeError: if it is not a node and not None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Returns string version of a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """Returns string version of singly linked list"""

        if self.__head is None:
            return ""
        temp = self.__head
        list_str = ""
        while temp is not None:
            list_str = list_str + str(temp.data)
            temp = temp.next_node
            if temp is not None:
                list_str = list_str + "\n"
        return list_str

    def sorted_insert(self, value):
        """Insert new Node to correct sorted position (increasing order)"""

        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        temp.next_node = Node(value, temp.next_node)
