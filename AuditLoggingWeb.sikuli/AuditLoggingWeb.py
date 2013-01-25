applicationPath = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
serverAddress = 'https://qa-six.calgaryscientific.com:8443'
screen = None

def connectToDatabase():
    return

def pressTab(numTimes):
    for i in xrange(0, numTimes):
        type('\t')

def startApp():
    print 'Starting browser...'
    openApp(applicationPath)
    # Shortcut to go to the address bar: CTRL+L
    print 'Navigating to test server...'
    wait(1)
    type("l", KEY_CTRL)
    type(serverAddress + '\n')
    wait(2)
    return

def login():
    print 'Logging into application...'
    wait(1)
    type('test30\tadmin\n')
    waitTime = 8
    wait(waitTime)
    pressTab(6)
    type('\n')
    wait(waitTime)
    return

def checkLoginMessages():
    return

def loadStudy():
    return

def performSearches():
    patient = 'lemon'
    print 'Performing search for patient \'' + patient + '\''
    type(patient)
    aFirefox = App("Firefox")
    with aFirefox:
        SCR1 = aFirefox.window().getScreen()
        screen.click(Pattern("SearchButton.png").similar(0.73))
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
    closeApp(applicationPath)
    print 'yay!'

if(__name__=="__main__"):
    SCREEN = Screen(1)
    main()