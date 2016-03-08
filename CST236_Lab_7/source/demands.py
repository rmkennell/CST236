import time
import getpass
def dateTime():
    return time.strftime("%c")

def openDoor():
    return 'I\'m afraid I can\'t do that' + ' ' + getpass.getuser()

def dogsOut():
    return getpass.getuser() + ' let the dogs out'


contacts = {
    'Sarah':    '503-235-7946',
    'Jason':    '971-359-7954',
    'Michael':  '531-473-9831',
    'Thomas':   '503-879-6375'

}

def contactLookup(name):

    if not isinstance(name, basestring):
        return "Invalid input"

    try:
        return contacts[name]
    except:
        return "No contact for " + name


def phoneLookup(number):

    if not isinstance(number, basestring):
        return "Invalid input"

    def find_key(val):
        return [k for k, v in contacts.iteritems() if v == val][0]

    try:
        return find_key(number)
    except:
        return "No name for " + number

