class Node: 
    def __init__(self, parent, value, depth):
        self.value = value
        self.depth = depth
        self.parent = parent
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
        
    def __str__(self):
        return str(self.value)
    
    def getGraph(self, graph):
        label = self.getLabel()
        
        graph.newItem()
        
    def display(self):
        print(f'Hello, my value is {self.value}, im {self.depth} levels deep')

        # if is not end node (has children) display them
        if not self.isEndNode():
            self.leftChild.display()
            self.middleChild.display()
            self.rightChild.display()        
        
        return
        
    # if this node has no children its the end node
    def isEndNode(self):
        return self.leftChild == None and self.middleChild == None and self.rightChild == None
    
    def getLabel(self):
        protagonist = self.isProtagonist()
        
        if protagonist == True:
            return ':)'
        
        return ':('
    
    def isProtagonist(self):
        return self.depth % 2 == 0
    
    # if node value is exactly 21 this node is tie result
    def isTie(self):
        return self.isEndNode() and self.value == 21
    
    # if node value is more than 21 this node is lose result
    def isLose(self):
        return self.isEndNode() and self.value > 21
    
    # if node value is less than 21 and has no children (will not happen)
    def isWin(self):
        return self.isEndNode() and self.value < 21
    
    def createChildren(self):
        # if node has value of 21 or more do not create children (game rules)
        if self.value >= 21:
            print('Can not create children')
            
            return
        
        self.addLeftChild()
        self.leftChild.createChildren()
        
        self.addMiddleChild()
        self.middleChild.createChildren()
        
        self.addRightChild()
        self.rightChild.createChildren()
        
        return
    
    def addLeftChild(self):
        childValue = self.value + 4
        childDepth = self.depth + 1
        
        self.leftChild = Node(self, childValue, childDepth)
        
        return
        
    def addMiddleChild(self):
        childValue = self.value + 5
        childDepth = self.depth + 1
        
        self.middleChild = Node(self, childValue, childDepth)
        
        return
    
    def addRightChild(self):
        childValue = self.value + 6
        childDepth = self.depth + 1
        
        self.rightChild = Node(self, childValue, childDepth)
        
        return
               