#Charlie Dakai
#COMP 340 HW5

class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(srcCode):
    tokSeq = []
    if srcCode[0] == "-":
        newToken = token("UNARY", "(0-1) *")
        tokSeq.append(newToken)
        srcCode = srcCode[1: ]
    while srcCode != "":
        char = srcCode[0]
        if char == "+":
            newToken = token("PLUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1: ]
        elif char == "-":
            if srcCode[1].isdigit() == False:
                newToken = token("UNARY", "0-1 *")
                tokSeq.append(newToken)
                srcCode = srcCode[1: ]
            else:
                newToken = token("MINUS", char)
                tokSeq.append(newToken)
                srcCode = srcCode[1: ]
        elif char == "*":
            newToken = token("MULTIPLICATION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1: ]
        elif char == "/":
            newToken = token("DIVISION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1: ]
        elif char == "(":
            newToken = token("LPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1: ]
        elif char == ")":
            newToken = token("RPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1: ]
        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1: ]
                if srcCode == "":
                    char = srcCode
                else:
                    char = srcCode[0]
            newToken = token("NUMBER", numbStr)
            tokSeq.append(newToken)
    return tokSeq
        