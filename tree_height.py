# python3
from collections import defaultdict, deque
import sys
import threading
import numpy
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []

def newNode(key):
    temp = Node(key)
    return temp

def insertNode(Node,key,parentKey):
    if Node.data == parentKey:
        child = newNode(key)
        Node.child.append(child)
        return 0
    else:
        j = 0 
        while j<len(Node.child):
            if insertNode(Node.child[j],key,parentKey) == 0:
                return 0
            j = j + 1
    return -1      

def compute_height(n, Node):
    # Write this function
    max_height = n
    # Your code here
    j = 0 
    while j < len(Node.child):
        childHeight = compute_height(n+1,Node.child[j])
        if max_height < childHeight:
            max_height = childHeight
        j = j + 1
    return max_height

def main():
    # implement input form keyboard and from files

    count = input() 
    
    elemList = [int(count)]
    i=0
    while i<int(count):
        element = input()
        elemList.append(int(element))
        i=i+1
    elemList.pop(0)

    i = 0
    root = newNode(-2)
    while i < len(elemList):
        if elemList[i] == -1:
            root.data = i 
            elemList[i] = -2
        elif elemList[i] > -1 and root.data != -2:
            if insertNode(root,i,elemList[i]) == 0:
                elemList[i] = -2
        else:
            pass
        i = i + 1
        if i == len(elemList):
            j = 0
            while j < len(elemList):
                if elemList[j] > -2:
                    i = 0
                j = j + 1    
    
    maxHeight = compute_height(1,root)
    print(maxHeight)

    
    #elemList=input()
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    pass
    #return line

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
main()


# print(numpy.array([1,2,3]))
