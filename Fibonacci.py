class FibNode:

    def __init__(self,element):
        self.element  = element
        self.prev= self
        self.next = self
        self.child = None
        self.parent = None
        self.degree = None
        self.marked = False

    def hasChild(self):
        return self.child != None

    def hasParent(self):
        return self.parent != None


class FibHeap:

    def __init__(self):
        self.root = None
        self.count = 0

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None
        self.count = 0

    def s_merge(self,heap ,otherheap):
        if heap==None:
            return otherheap
        if otherheap==None:
            return heap

        if heap.element>otherheap.elemenet:
            temp = heap
            heap = otherheap
            otherheap = temp

        heap_next = heap.next
        other_prev = otherheap.prev
        heap.next = otherheap
        otherheap.prev = heap
        heap_next.prev = other_prev
        other_prev.next = heap_next
        return heap


    def insert(self,element):
        node = FibNode(element)
        node.element = element
        node.prev = node
        node.next = node
        node.degree = 0
        node.marked = False
        node.child = None
        node.parent = None

        return self.s_merge(self.root,node)


    def merge(self,other):
        self.root = self.s_merge(self.root,other.root)
        other.clear()

    def getMin(self):
        return self.root.element

    def removeMin(self):
        old = self.root
        _unmarkandunParentAll(self.root.child);

        if self.root.next==self.root:
            self.root = self.root.child
        else:
            self.root.next.prev = self.root.prev
            self.root.prev.next = self.root.next
            self.root = self.s_merge(self.root.next,self.root.child)

        if self.root == None:
            return self.root


        trees = list()
        for i in range(0,64):
            trees.append(list())

        while(True):
            if trees[self.root.degree] != None:
                t = trees[self.root.degree]

                if t==self.root :
                    break

                trees[self.root.degree] = None

                if self.root.element < t.element :
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    addChild(self.root,t)
                else:
                    t.prev.next = t.next
                    t.next.prev = t.prev

                    if self.root.next == self.root:
                        t.next = t.prev = t
                        addChild(t,self.root)
                        self.root = t
                    else:
                        self.root.prev.next = t
                        self.root.next.prev = t
                        t.next = self.root.next
                        t.prev = self.root.prev
                        addChild(t,self.root)
                        self.root = t
                continue
            else:
                trees[self.root.degree] = self.root

            self.root = self.root.next

        min = self.root

        i = 1
        while True:
            if self.root.element < min.element :
                min = self.root







