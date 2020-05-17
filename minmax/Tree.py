from Node import Node
import gvgen

class Tree:
    def __init__(self):
        self.root = None
        
    def initializeTree(self):
        if self.root != None:
            print('Already created!')
            
            return
        
        root = Node(None, 0, 0)
        root.createChildren()
        
        self.root = root
        
        return
        
    def displayTree(self):
        self.root.display()
        
        return
    
    def getGraph(self):
        graph = gvgen.GvGen()
        
        if self.root == None:
            print('No root node, could not get graph')
            
            return
        
        self.root.addToGraph(graph)
        
        return graph