class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)
        
    def reverseList(self):
        node = None
        head = self.head
        while(head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        self.head= node





linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node


linked_list.printList()
linked_list.reverseList()
linked_list.printList()
