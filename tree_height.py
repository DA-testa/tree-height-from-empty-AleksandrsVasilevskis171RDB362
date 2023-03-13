# python3

#from collections import defaultdict, deque
import sys
import threading
import numpy

#конструктор


count=" "
i = 0
 
class Node:
    def __init__(self, data, dataElement):
        self.dataElement = dataElement
        self.data = data
        self.child = []

def newNode(key,dataElement):
    temp = Node(key,dataElement)
    return temp

def insertNode(Node,key,parentKey):
    if Node.data == parentKey:
        child = newNode(key,parentKey)
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

def prtinTree(root, level = 0):
    
    print("level of range",level)
    print( root.dataElement)
    for child in root.child:
        prtinTree(child, level+1)


def mehanism (elemList=[]):

    len(elemList)
    Node = newNode(-2,-2)
    i = 0
    while i < len(elemList):
        if elemList[i] == -1:
            Node.data = i 
            Node.dataElement = -1
            elemList[i] = -2
        elif int(elemList[i]) > -1 and Node.data != -2:
            if insertNode(Node,i,elemList[i]) == 0:
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
    maxHeight=compute_height(1,Node)
    print(maxHeight)
    #
    # 
    # prtinTree(Node)



def  main():

    choice = input()
    if "I" in choice:
        count = input() 
        elements = input()
        elemList = []
        elemList = elements.split()
        elemListInt=[]
        for i in elemList:
           elemListInt.append(int(i))
        if int(count)== len(elemListInt):   
            #print(elemListInt)
            mehanism(elemListInt)
        else:
            print("ERROR")
            pass
        
        #prtinTree("node is",mehanism(elemListInt))
    elif "F" in choice:

       # print("F")
        nameOfFille = input()
       
        for i in nameOfFille:
            if i == "a":
                print("ERROR")
                return 0
            
              
        url = r"test//"
        realUrl = url + nameOfFille
        #print("yyy",realUrl)
        f = open(realUrl)        

       # print("2")
        readFileArray = f.read().splitlines()
        elementCount=int(readFileArray[0])
        #print(readFileArray)
               #print(ele)
        #print(elementCount)
        arrList = readFileArray[1]

        arrList = arrList.split()
       # print (arrList)
        arrListInt = []
        for i in arrList:
            arrListInt.append(int(i)) 
        ##print (arrListInt)
        mehanism(arrListInt)

               
    else:
        print("ERROR")
        pass        
     
    #implement input form keyboard and from files
    
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
  #  return elemList
    #pass
   


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
t=threading.Thread(target=main)
t.start()





#print(count)
#main()

#print(count)

#mehanism(elemList)
#root = mehanism(elemList)
    
#maxHeight = compute_height(1,root)
#print(maxHeight)
#prtinTree(root)



# print(numpy.array([1,2,3]))
