def isUserAuthorized(usercreds, username, password):
    isUser = False
    usercreds.lock()
    for i in range(len(usercreds)):
        if(usercreds[i][0] == username and usercreds[i][1] == password):
            isUser = True
            break
    usercreds.unlock()
    return isUser