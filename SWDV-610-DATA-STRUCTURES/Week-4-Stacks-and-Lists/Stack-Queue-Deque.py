# https://pythonhosted.org/pyllist/
# This module implements linked list data structures.
# Currently two types of lists are supported:
# a doubly linked dllist and a singly linked sllist.
# $ pip install pyllist

from pyllist import sllist

from random import randint


# 1. Implement a STACK using linked lists
# https://ece.uwaterloo.ca/~dwharder/aads/Abstract_data_types/Linear_ordering/Stack/

class GRStack(object):

    def __init__(self):
        self.__lnkdlist = sllist()

    def push(self, item):
        self.__lnkdlist.appendleft(item)

    def top(self):  # peek
        return self.__lnkdlist.first()

    def pop(self):
        return self.__lnkdlist.popleft()

    @property
    def size(self):
        return self.__lnkdlist.size

    @property
    def isEmpty(self):
        return self.size == 0


# 2. Implement a QUEUE using linked lists
# https://ece.uwaterloo.ca/~dwharder/aads/Abstract_data_types/Linear_ordering/Queue/
# The functions are also referred to as void enqueue( Type ), Type head() const, and void dequeue(), respectively.


class GRQueue(object):

    def __init__(self):
        self.__lnkdlist = sllist()

    def push(self, item):  # enqueue
        self.__lnkdlist.appendright(item)

    def front(self):
        return self.__lnkdlist.first()

    def pop(self):  # dequeue
        return self.__lnkdlist.popleft()

    @property
    def size(self):
        return self.__lnkdlist.size

    @property
    def isEmpty(self):
        return self.size == 0


# 3. Implement a DEQUE using linked lists
# https://ece.uwaterloo.ca/~dwharder/aads/Abstract_data_types/Linear_ordering/Deque/
# The functions are also referred to as void enqueue_head( Type ), Type head() const, void dequeue_head(),
# void enqueue_tail( Type ), Type tail() const, and void dequeue_tail(), respectively.

class GRDeque(object):

    def __init__(self):
        self.__lnkdlist = sllist()

    def push_front(self, item):
        self.__lnkdlist.appendleft(item)

    def front(self):
        return self.__lnkdlist.first()

    def pop_front(self):
        return self.__lnkdlist.popleft()

    def push_back(self, item):
        self.__lnkdlist.appendright(item)

    def back(self):
        return self.__lnkdlist.last()

    def pop_back(self):
        return self.__lnkdlist.popright()

    @property
    def size(self):
        return self.__lnkdlist.size

    @property
    def isEmpty(self):
        return self.size == 0


def main():
    stack = GRStack()
    queue = GRQueue()
    deque = GRDeque()

    items = [randint(-10, 50) for i in range(20)]

    print("Original Array: ", items, "\n")

    print("Stack and Queue insertion oder: ", end="")
    for item in items:
        stack.push(item)
        queue.push(item)
        print(item, ", ", end="")
    print("\n")

    print("Deque insertion (alternated) order: ", end="")
    for item in items:
        if deque.size % 2 == 0:
            deque.push_front(item)
            print(item, " (front), ", end="")
        else:
            deque.push_back(item)
            print(item, " (back), ", end="")
    print("\n")

    print("Stack popping order: ", end="")
    while not stack.isEmpty:
        print(stack.pop(), ", ", end="")
    print("\n")

    print("Queue popping order: ", end="")
    while not queue.isEmpty:
        print(queue.pop(), ", ", end="")
    print("\n")

    print("Deque popping order: ", end="")
    while not deque.isEmpty:
        print(deque.pop_front(), ", ", end="")
    print("\n")


main()
