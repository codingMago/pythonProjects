command = "G()(al)"

def interpret(command):
    pHolder = ""
    sHolder = ""

    for i in command:
        if "(" in sHolder:
            if i == ")":
                pHolder += "o"
            elif i == "a":
                return

        if i == "G":
            pHolder += i
        elif i == "(":
            sHolder += i
        


