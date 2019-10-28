import sys,datetime

from profile import Profile
from message import Message
from db import Db

class Inbox:
    def __init__(self,profile):
        self.db = Db()
        self.profile=self.getOrCreateProfileByUser(profile)

    def getOrCreateProfileByUser(self,user):
        profile=Profile()
        self.db.profile.loadByUser(profile,user)
        profile.status = 1
        profile.user = user
        self.db.profile.save(profile)
        return profile

    def show(self):
        print("inbox for " + self.profile.user)
        print("TODO")

def inbox(user):
    inbox = Inbox(user)
    inbox.show()

def testInbox():
    inbox("bob")

def main():
    args = sys.argv
    args.pop(0)
    if len(args) == 0:
        testInbox()
    else:
        inbox(*args)

if __name__ == '__main__':
    main()
