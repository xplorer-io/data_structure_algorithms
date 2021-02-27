class Node:
    """
    This is a single node

    Attributes
    -----------
    data: int
        Data contained in a single node.
    next: int
        Reference to the next node.
    prev: int
        Reference to the previous node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly Linked list

    Attributes
    -----------
    head: int
        Pointer pointing to head of the list
    tail: int
        Pointer pointing to tail of the list

    Methods
    ---------

    insert_at_empty : 
        Inserts element when list if empty

    insert_at_first : 
        Insert element at first of the list

    insert_at_nposition: 
        Insert element at n poistion (middle)

    insert_at_end: 
        Insert element at end

    delete at pos: 
        Delete element at n position (eg. 1 for deleting element at first)

    display_list: 
        Display doubly linked list

    display_list_rev: 
        Display doubly linked list in reverse.

    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_empty(self,data):
        print()
        print("List empty !!!")
        print()
        print("Creating new node")
        new_node = Node(data)
        print("Adding node with data "+str(data)+" to the list")
        # If list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.tail.next = None

    def insert_at_first(self,data):
        if self.head == None:
            self.insert_at_empty(data)
        else:
            print()
            print("Creating new node")
            new_node = Node(data)
            print("Adding node with data "+str(data)+" to the list")
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_nposition(self, data, pos):
        print()
        print("Creating new node")
        new_node = Node(data)
        if self.head == None:
            self.insert_at_empty(data)
        else:
            print("Adding node with data "+str(data)+" after the "+str(pos)+"th position")
            c = 1
            t = self.head
            length_of_list = self.count_list()
            while self.head != None:
                if c == pos:
                    new_node.next = self.head.next
                    self.head.next.prev = new_node
                    self.head.next = new_node
                    new_node.prev = self.head
                c = c + 1
                self.head = self.head.next
            self.head = t

    def insert_at_end(self, data):
        print()
        print("Creating new node")
        new_node = Node(data)
        # If list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
        # Insertion at end
            print("Adding node with data "+str(data)+" to the end of the list")
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

    def display_list(self):
        temp = self.head
        if self.head == None:
            print("List is empty")
            return
        print("Final Doubly linked List :", end=' ')
        while self.head != None:
            print(self.head.data,end=' ')
            self.head = self.head.next
        self.head = temp

    def display_list_rev(self):
        temp = self.head
        tail_temp = self.tail
        if self.head == None:
            print("List is empty")
            return
        print("Final Doubly linked List in reverse:", end=' ')
        while self.tail != self.head:
            print(self.tail.data,end=' ')
            self.tail = self.tail.prev
        print(self.tail.data, end=' ')
        self.head = temp
        self.tail = tail_temp

    def count_list(self):
        count = 0
        temp = self.head
        while self.head != None:
            count = count + 1
            self.head = self.head.next
        self.head = temp
        return count

    def delete_at_pos(self, pos):
        print()
        temp = self.head
        if self.head == None:
            print("List is empty")
            return
        if pos == 1:
            print("Deleting node at "+str(pos)+"st position")
            self.head.next.prev = None
            self.head = self.head.next
        elif pos == self.count_list():
            print("Deleting node at "+str(pos)+" position")
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            print("Deleting node at "+str(pos)+" position")
            c = 1
            while self.head != None:
                if c == pos:
                    self.head.prev.next = self.head.next
                    self.head.next.prev = self.head.prev
                c = c + 1
                self.head = self.head.next
        self.head = temp
        
    def delete_at_end(self):
        print()
        print("Deleting node at the end")
        if self.head == None:
            print("List is empty")
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev

if __name__=="__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_empty(50)
    doubly_linked_list.insert_at_first(10)
    doubly_linked_list.insert_at_end(20)
    doubly_linked_list.insert_at_end(40)
    doubly_linked_list.insert_at_end(70)
    doubly_linked_list.insert_at_nposition(23,3)
    doubly_linked_list.insert_at_nposition(27,3)
    print()
    doubly_linked_list.display_list()
    print()
    doubly_linked_list.display_list_rev()
    print()
    doubly_linked_list.delete_at_pos(3)
    print()
    doubly_linked_list.display_list()
    print()
    doubly_linked_list.display_list_rev()
    print()
    doubly_linked_list.delete_at_end()
    print()
    doubly_linked_list.display_list()
    print()
    doubly_linked_list.display_list_rev()
    print()