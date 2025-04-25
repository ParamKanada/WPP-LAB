'''1. Write a Python program to create a class representing a linked list data structure. Include
methods for displaying linked list data, inserting and deleting nodes.'''
class Node: #the stucture of the node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if not self.head:   #if head is not null, then assign new node to head
            self.head = new_node
            return
        
        last = self.head #if head is not empty,then traverse the ll
        while last.next:
            last = last.next
        last.next = new_node    #new node becomes the last node

    def delete(self, data):
        temp = self.head

        if temp and temp.data == data:  #if head contains the data to be deleted,
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Key not found")
            return

        prev.next = temp.next
        temp = None

#trversal of linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

llist = LinkedList()
llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.display()

llist.delete(20)
llist.display()

llist.delete(40)