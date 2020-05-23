class Node: 
    def __init__(self, parent, value, depth):
        self.value = value
        self.depth = depth
        self.parent = parent
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
        self.graphItem = None
        self.result = None
        self.selected = None
        
    def __str__(self):
        return str(self.value)
    
    def getMoves(self):
        if self.isEndNode():
            return self.getEndResult()
        
        if self.isProtagonist():
            child = self.getChildWithHighestResult()
        else:
            child = self.getChildWithLowestResult()
            
        child.setSelected(True)
        
        self.setEndResult(child.getEndResult())
            
        return child.getEndResult()
            
    def getChildrenList(self):
        return list([self.leftChild, self.middleChild, self.rightChild])
    
    def getChildrenEndResults(self):
        leftResult = self.leftChild.getMoves()
        middleResult = self.middleChild.getMoves()
        rightResult = self.rightChild.getMoves()
        
        return list([leftResult, middleResult, rightResult])
    
    def getChildWithHighestResult(self):
        maxResult = max(self.getChildrenEndResults())
        
        for child in self.getChildrenList():
            if child.getEndResult() == maxResult:
                return child

    def getChildWithLowestResult(self):
        minResult = min(self.getChildrenEndResults())
        
        for child in self.getChildrenList():
            if child.getEndResult() == minResult:
                return child
            
    # add node to graph
    def addToGraph(self, graph, parentGraphNode = None):
        label = self.getLabel()
        
        self.graphItem = graph.newItem(label)
        
        # if this node is root node it has no parent, do not create a link
        if not self.isRootNode() and parentGraphNode != None:
            nodeLink = graph.newLink(parentGraphNode, self.graphItem)
            graph.propertyAppend(nodeLink, 'label', self.value)
            
            # if this node is selected by parent node check if parent node is protagonist or antagonist and color the line accordingly
            if self.selected == True:
                graph.propertyAppend(nodeLink, 'color', self.getParentLinkColor())
        
        # if has no children exit recursion
        if self.isEndNode():
            return
        
        self.leftChild.addToGraph(graph, self.graphItem)
        self.middleChild.addToGraph(graph, self.graphItem)
        self.rightChild.addToGraph(graph, self.graphItem)
        
        return
    
    def getParentLinkColor(self):
        if (self.parent.isProtagonist()):
            return '#7befb2'
        
        return '#f03434'
    
    def calculateEndResultByValue(self):
        if self.isTie():
            return 0
            
        if self.isLose():
            return -1
        
    def getEndResult(self):
        return self.result
        
    def setEndResult(self, result):
        self.result = result
        
        return
        
    def setSelected(self, selected):
        self.selected = selected
        
        return
        
    def display(self):
        print(f'Hello, my value is {self.value}, im {self.depth} levels deep')

        # if is end node (has no children) exit
        if self.isEndNode():
            return

        self.leftChild.display()
        self.middleChild.display()
        self.rightChild.display()        
        
        return
        
    # get label ( ':('  ':)' TIE or LOSE ) depending on if this node is protagonist, antagonist or end node
    def getLabel(self):
        # if is end node return label describing if this node is lose or tie node
        if self.isEndNode():
            return self.getEndNodeLabel()
        
        protagonist = self.isProtagonist()
        
        if protagonist == True:
            return ':)'
        
        return ':('
    
    def getEndNodeLabel(self):
        if self.isTie():
            return f'TIE: {self.getEndResult()}'
        
        if self.isLose():
            return f'LOSE: {self.getEndResult()}'
        
        # if is end node but is not tie nor lose then wtf
        return 'what am i'
    
    # return true, if node is root node (depth = 0)
    def isRootNode(self):
        return self.depth == 0
    
    # if this node has no children its the end node
    def isEndNode(self):
        return self.leftChild == None and self.middleChild == None and self.rightChild == None
    
    def isProtagonist(self):
        return self.depth % 2 == 0
    
    # if node value is exactly 21 this node is tie result (game rules)
    def isTie(self):
        return self.isEndNode() and self.value == 21
    
    # if node value is more than 21 this node is lose result (game rules)
    def isLose(self):
        return self.isEndNode() and self.value > 21
    
    def createChildren(self):
        # if node has value of 21 or more do not create children (game rules). It is a end node then
        if self.value >= 21:
            print('Can not create children, getting end result')
            
            result = self.calculateEndResultByValue()
            
            self.setEndResult(result)
            
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
               