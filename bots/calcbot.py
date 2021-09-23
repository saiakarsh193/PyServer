def calcbot_get_precedence(a, b):
    preclist = [["^", 4], ["*", 3], ["/", 3], ["+", 2], ["-", 2], ["(", 0], [")", 0]]
    for i in range(len(preclist)):
        if(a == preclist[i][0]):
            a = preclist[i][1]
        if(b == preclist[i][0]):
            b = preclist[i][1]
    if(a > b):
        return True
    else:
        return False

def calcbot(message):
    var = ""
    inv = False
    lastdig = ""
    openbrac = 0
    closebrac = 0
    for i in range(len(message)):
        if(message[i] != " "):
            if(message[i].isdigit() or message[i] == '+' or message[i] == '-' or message[i] == '*' or message[i] == '/' or message[i] == '(' or message[i] == ')'):
                var += message[i]
            else:
                inv = True
            lastdig = message[i]
        if(message[i] == "("):
            openbrac += 1
        elif(message[i] == ")"):
            closebrac += 1
        if(closebrac > openbrac):
            inv = True
    if(inv or not message or openbrac != closebrac or not(lastdig.isdigit() or lastdig == ")")):
        return "Invalid Input"

    # shunting yard algorithm
    eqn = ""
    stk = []
    isDig = False
    for i in range(len(var)):
        if(var[i].isdigit()):
            if(not isDig):
                eqn += " "
            isDig = True
            eqn += var[i]
        else:
            isDig = False
            if(var[i] == '+' or var[i] == '-' or var[i] == '*' or var[i] == '/'):
                while(len(stk) > 0 and not(calcbot_get_precedence(var[i], stk[len(stk) - 1]))):
                    eqn += " " + stk.pop()
                stk.append(var[i])
            elif(var[i] == '('):
                stk.append(var[i])
            elif(var[i] == ')'):
                while(len(stk) > 0 and stk[len(stk) - 1] != '('):
                    eqn += " " + stk.pop()
                stk.pop()
    while(len(stk) > 0):
        eqn += " " + stk.pop()
    
    stk = eqn.strip().split(' ')
    ans = []
    for i in range(len(stk)):
        if(stk[i] == '+' or stk[i] == '-' or stk[i] == '*' or stk[i] == '/'):
            tb = ans.pop()
            ta = ans.pop()
            if(stk[i] == '+'):
                ta = ta + tb
            elif(stk[i] == '-'):
                ta = ta - tb
            elif(stk[i] == '*'):
                ta = ta * tb
            elif(stk[i] == '/'):
                ta = int(ta / tb)
            ans.append(ta)
        else:
            ans.append(int(stk[i]))
    return str(ans[0])
