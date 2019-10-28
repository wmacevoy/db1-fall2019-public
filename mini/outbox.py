import sys,datetime

from profile import Profile
from message import Message
from db import Db

class Outbox:
    def __init__(self,user):
        self.db = Db()
        self.profile=self.getOrCreateProfileByUser(user)

    def getOrCreateProfileByUser(self,user):
        profile=Profile()
        self.db.profile.loadByUser(profile,user)
        profile.status = 1
        profile.user = user
        self.db.profile.save(profile)
        return profile

    def show(self):
        print("outbox for " + self.profile.user)
        print("TODO")

def outbox(user):
    inbox = Outbox(user)
    inbox.show()

def testInbox():
    outbox("alice")

def main():
    args = sys.argv
    args.pop(0)
    if len(args) == 0:
        testInbox()
    else:
        outbox(*args)

if __name__ == '__main__':
    main()
