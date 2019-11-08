import sys,dbdatetime

from profile import Profile
from message import Message
from db import Db

class Reader:
    def __init__(self,user,messageid):
        self.db = Db()
        self.profile=self.getOrCreateProfileByUser(user)
        self.messageid=messageid

    def getOrCreateProfileByUser(self,user):
        profile=Profile()
        self.db.profile.loadByUser(profile,user)
        profile.status = 1
        profile.user = user
        self.db.profile.save(profile)
        return profile

    def read(self):
        print("read message")

def read(user,messageid):
    reader = Reader(user,messageid)
    reader.read()

def testRead():
    read("bob",1)

def main():
    args = sys.argv
    args.pop(0)
    if len(args) == 0:
        testRead()
    else:
        read(*args)

if __name__ == '__main__':
    main()
