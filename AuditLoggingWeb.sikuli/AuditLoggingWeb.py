applicationPath = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
serverAddress = 'https://qa-six.calgaryscientific.com:8443'

def connectToDatabase():
    return

def startApp():
    openApp(applicationPath)
    # Shortcut to go to the address bar: CTRL+L
    wait(1)
    type("l", KEY_CTRL)
    type(serverAddress + '\n')
    return

def login():
    wait(1)
    type('test30\tadmin\n')
    wait(10)
    exists("nf.png", 5)
    return

def checkLoginMessages():
    return

def loadStudy():
    return

def performSearches():
    return

def checkSearchMessages():
    return

def checkLoadingMessages():
    return

def logout():
    return

def checkLogoutMessage():
    return

def main():
    connectToDatabase()
    startApp()
    login()
    checkLoginMessages()
    performSearches()
    checkSearchMessages()
    loadStudy()
    checkLoadingMessages()
    logout()
    checkLogoutMessage()
    print 'yay!'

if(__name__=="__main__"):
    main()