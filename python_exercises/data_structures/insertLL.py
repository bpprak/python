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

    # list start at 0
    #get the insert node
    #check if the list is empty
    #check for general cases
     #get previous, and get next node 
     #put the new element in between 
    def insertNode(self, val, pos):
        target = Node(val)
        if(pos == 0):
            target.next = self.head
            self.head = target
            return

        def getPrev(pos):
            temp = self.head
            count = 1
            while(count < pos):
                temp = temp.next
                count += 1
            return temp

        prev = getPrev(pos)
        nextNode = prev.next

        prev.next = target
        target.next = nextNode
        
    def reverseList(self, head: Node) -> Node:
        node = None
        while(head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        return node


# List Structure : 5 => 1 => 3 => 7
linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.insertNode(2, 2)
linked_list.printList()

