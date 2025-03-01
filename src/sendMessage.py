from pywhatkit import sendwhatmsg_instantly

def sendMessage (phone, message):
    sendwhatmsg_instantly(phone, message, 10, True)