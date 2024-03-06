
# Charlie Dakai


def decipher(babyExp):
    srcCode = ""
    while babyExp != "":
        if babyExp[0] == "p":
            srcCode += "+"
            babyExp = babyExp[3:]
        elif babyExp[0] == " ":
            babyExp = babyExp[1:]
        elif babyExp[0] == "g":
            srcCode += "-"
            babyExp = babyExp[3:]
        elif babyExp[0] == "h":
            srcCode += "/"
            babyExp = babyExp[3:]
        elif babyExp[0] == "d":
            srcCode += ")"
            babyExp = babyExp[4:]
        elif babyExp[0:10] == "baaaaaaaaa":
            srcCode += "9"
            babyExp = babyExp[10:]
        elif babyExp[0:9] == "baaaaaaaa":
            srcCode += "8"
            babyExp = babyExp[9:]
        elif babyExp[0:8] == "baaaaaaa":
            srcCode += "7"
            babyExp = babyExp[8:]
        elif babyExp[0:7] == "baaaaaa":
            srcCode += "6"
            babyExp = babyExp[7:]
        elif babyExp[0:6] == "baaaaa":
            srcCode += "5"
            babyExp = babyExp[6:]
        elif babyExp[0:5] == "baaaa":
            srcCode += "4"
            babyExp = babyExp[5:]
        elif babyExp[0:4] == "baaa":
            srcCode += "3"
            babyExp = babyExp[4:]
        elif babyExp[0:3] == "baa":
            srcCode += "2"
            babyExp = babyExp[3:]
        elif babyExp[0:2] == "ba":
            srcCode += "1"
            babyExp = babyExp[2:]
        elif babyExp[0:4] == "milk":
            srcCode += "*"
            babyExp = babyExp[4:]
        elif babyExp[0:4] == "mama":
            srcCode += "("
            babyExp = babyExp[4:]
        elif babyExp[0] == "b":
            srcCode += "0"
            babyExp = babyExp[1:]
        else:
            return "Invalid Input"
    return srcCode




