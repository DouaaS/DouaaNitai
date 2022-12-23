from avl_template_new import AVLTreeList
import time
import csv
import random


# Creating a node class
class Node:
    def __init__(self, data):
        self.data = data  # adding an element to the node
        self.next = None  # Initally this node will not be linked with any other node
        self.prev = None  # It will not be linked in either direction


# Creating a doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initally there are no elements in the list
        self.tail = None
        self.len = 0

    def push_front(self, new_data):  # Adding an element before the first element
        new_node = Node(new_data)  # creating a new node with the desired value
        new_node.next = self.head  # newly created node's next pointer will refer to the old head

        if self.head != None:  # Checks whether list is empty or not
            self.head.prev = new_node  # old head's previous pointer will refer to newly created node
            self.head = new_node  # new node becomes the new head
            new_node.prev = None

        else:  # If the list is empty, make new node both head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None  # There's only one element so both pointers refer to null
        self.len += 1

    def push_back(self, new_data):  # Adding an element after the last element
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:  # checks whether the list is empty, if so make both head and tail as new node
            self.head = new_node
            self.tail = new_node
            new_node.next = None  # the first element's previous pointer has to refer to null

        else:  # If list is not empty, change pointers accordingly
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node  # Make new node the new tail
        self.len += 1


    def insert(self, i, new_data):  # Inserting a new node in i
        new_node = Node(new_data)
        curr = None
        if i == 0:
            self.push_front(new_node)
            return
        if i == self.len:
            self.push_back(new_node)
            return
        if i <= self.len//2:
            curr = self.head
            for i in range(self.len//2-1):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.len // 2):
                curr = curr.prev
        tmp = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = tmp
        tmp.prev = new_node
        self.len += 1

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next


def q2_at_start(file):
    a = []
    l = DoublyLinkedList()
    t = AVLTreeList()
    file.writerow(['start'])
    file.writerow(["i","array","linkedlist","tree"])
    for i in range(1,11):
        n = 1500*i

        t0 = time.perf_counter()
        for j in range(n):
            a.insert(0,j)
        t1 = time.perf_counter()
        arr_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            l.push_front(j)
        t1 = time.perf_counter()
        lst_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            t.insert(0,j)
        t1 = time.perf_counter()
        tree_time = (t1 - t0)/n

        file.writerow([i,arr_time,lst_time, tree_time])
    file.writerow("")


def q2_at_end(file):
    a = []
    l = DoublyLinkedList()
    t = AVLTreeList()
    file.writerow(['end'])
    file.writerow(["i","array","linkedlist","tree"])
    for i in range(1,11):
        n = 1500*i

        t0 = time.perf_counter()
        for j in range(n):
            a.append(j)
        t1 = time.perf_counter()
        arr_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            l.push_back(j)
        t1 = time.perf_counter()
        lst_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            t.insert(t.length(),j)
        t1 = time.perf_counter()
        tree_time = (t1 - t0)/n

        file.writerow([i,arr_time,lst_time, tree_time])
    file.writerow("")



def q2_at_random(file):
    a = []
    l = DoublyLinkedList()
    t = AVLTreeList()
    file.writerow(['random'])
    file.writerow(["i","array","linkedlist","tree"])
    for i in range(1,11):
        n = 1500*i

        t0 = time.perf_counter()
        for j in range(n):
            k = random.randint(0,len(a))
            a.insert(k,j)
        t1 = time.perf_counter()
        arr_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            k = random.randint(0,l.len)
            l.insert(k,j)
        t1 = time.perf_counter()
        lst_time = (t1 - t0)/n

        t0 = time.perf_counter()
        for j in range(n):
            k = random.randint(0, t.length())
            t.insert(k,j)
        t1 = time.perf_counter()
        tree_time = (t1 - t0)/n

        file.writerow([i,arr_time,lst_time, tree_time])
    file.writerow("")




def q2_all():
    o = open("output.csv", "w")
    writer = csv.writer(o)
    q2_at_start(writer)
    q2_at_end(writer)
    q2_at_random(writer)
    o.close()
    print('done!')


q2_all()
