from pythonds.basic.stack import Stack

c = Stack()


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
H = HashTable()
H[11] = 'chenglong'
H[111] = 'll'
print(H.size)
print(H.data)
print(H[0])

import time
def bubbleSort(alist):
    start = time.time()


    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    end = time.time()
    return (end-start)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ff=[2,4,8,1,4,8,9,2,6,45,32,66,23,67,232,646,22,344,2234,234,342,234,2334,234,234,234,234,234,234]
d=bubbleSort(ff)



'''回文检查：list首位对比循环'''


def palchacker(aString):
    chardeque = []

    for ch in aString:
        chardeque.append(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque[0]
        last = chardeque[len(chardeque) - 1]
        chardeque.pop()
        chardeque.pop(0)

        if first != last:
            stillEqual = False

    return stillEqual


print(palchacker('shkgjgkhs'))
print(palchacker('chaaaafaaaahc'))

'''顺序查找'''
def sequentialsearch(blist, item):
    pos = 0
    found = False
    while pos < len(blist) and not found:
        if blist[pos] == item:
            found = True

        else:
            pos = pos + 1

    return found


print(sequentialsearch(alist, 20))
ff=[2,4,8,1,4,8,9,2,6,45,32,66,23,67,232,646,22,344,2234,234,342,234,2334,234,234,234,234,234,234]
print(len(ff))


'''冒泡排序傻瓜代码，第一次写嘻嘻'''
def bubbleSort1(list):
    start=time.time()
    for j in range(0,len(list)):
        for i in range(0,(len(list)-j-1)):

            if list[i]>list[i+1]:

                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp

            i=i+1



    j=j+1
    end=time.time()
    return (end-start)

d1=bubbleSort1(ff)
print(d1)
print(d)
cc=0
for i in range(3040000):
    if d>=d1:
        cc=cc+1
    else:
        cc=cc-1

print('\33[5;31;40mfff\033[5m'+str(cc))


class BinaryTree:

    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)

        else:
            t=self.leftChild
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = self.rightChild
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return  self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setVal(self,obj):
        self.key=obj
    def getVal(self):

       return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

r = BinaryTree('a')
print(r.getVal())
b=BinaryTree('///////////////////////////////////////////////////////////')
print(b.getVal())
r.insertLeft('b')
print(r.leftChild.getVal())
r.leftChild.insertLeft('c')
print(r.leftChild.leftChild.getVal())


from pythonds.basic.stack import Stack


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

#pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#pt.postorder()  #defined and explained in the next section
#pt.preorder()
from pythonds.trees.binheap import BinHeap

bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())F

from pythonds.graphs import Graph
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
g=Graph()
for i in range(6):
    g.addVertex(i)