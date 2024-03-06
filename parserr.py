#Charlie Dakai
#HW6 COMP 340

class treeNode:
    def __init__(self,type,value,precedence):
        self.type = type
        self.value = value
        self.precedence = precedence
    parent = None
    lChild = None
    rChild = None


def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence
    
def createTreeNodeList(tokSeq):
    treeNodeList = []
    if type == "LPAREN":
        for token in tokSeq:
            if type.isdigit() == False:
                if type == "PLUS":
                    precedence == precedence + 4
                elif type == "MINUS":
                    precedence == precedence + 4
                elif type == "MULTIPLICATION":
                    precedence = precedence + 4
                elif type == "DIVISION":
                    precedence = precedence + 4
    if type == "RPAREN":
        for token in tokSeq:
            if type.isdigit() == False:
                if type == "PLUS":
                    precedence == precedence - 4
                elif type == "MINUS":
                    precedence == precedence - 4
                elif type == "MULTIPLICATION":
                    precedence = precedence - 4
                elif type == "DIVISION":
                    precedence = precedence - 4
    for token in tokSeq:        
        newNode = treeNode(token.type, token.value, getPrecedence(token.type))
        treeNodeList.append(newNode)
    return treeNodeList

def parse(tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    rootNode = findRoot(treeNodeList)
    return rootNode

def parsing(treeNodeList):
    dummyNode = treeNode("Dummy", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)
    if len(treeNodeList) == 3:
        return treeNodeList[1]
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index-1]
            rOp = treeNodeList[index+1]
            if rOp.precedence > lOp.precedence:
                #right
                rOp.lChild = node
                node.parent = rOp
                lOp.rChild = rOp
                rOp.parent = lOp
            else:
                #left
                lOp.rChild = node
                node.parent = lOp
            if rOp.type != "Dummy":
                while lOp.parent != None:
                    if lOp.parent.precedence < rOp.precedence:
                        break
                    lOp = lOp.parent
                if lOp.parent != None:
                    lOp.parent.rChild = rOp
                    rOp.parent = lOp.parent
                rOp.lChild = lOp
                lOp.parent = rOp

def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if node.parent == None and node.type != "Dummy":
            rootNode = node
            break
    return rootNode

def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        #operand
        print("i am in print tree here")
        print(rootNode.value, end="")
    else:
        #operator
        print("(", end="")
        printTree(rootNode.lChild)
        print(rootNode.value, end="")
        printTree(rootNode.rChild)
        print(")", end ="")


