#Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def __init__(self):
        self.head = None
        

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.val) + " ")
            temp = temp.next
        print(linked_list)

    def mergeTwoLists(self, l1: Node, l2:Node):
        cur = Node(0)
        ans = cur

        while(l1 and l2):
            if(l1.val > l2.val):
                cur.next = l2
                l2 = l2.next

            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        self.head= ans.next



l1 = Solution()
l1.head = Node(1)

second_node = Node(2)
third_node = Node(4)


l1.head.next = second_node
second_node.next = third_node

l2 = Solution()
l2.head = Node(1)

second_node = Node(3)
third_node = Node(4)


l2.head.next = second_node
second_node.next = third_node

Object = Solution()
Object.mergeTwoLists(l1.head,l2.head)
Object.printList()

