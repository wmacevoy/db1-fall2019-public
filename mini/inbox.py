import sys,dbdatetime

from profile import Profile
from message import Message
from db import Db

class Inbox:
    def __init__(self,user):
        self.db = Db()
        self.user = user
        self.profile=self.getOrCreateProfileByUser(user,None)

    def getOrCreateProfileByUser(self,user,status):
        profile=Profile()
        self.db.profile.loadByUser(profile,user)
        if status != None:
            profile.status = status
        profile.user = user
        self.db.profile.save(profile)
        return profile

    def getProfileById(self,id):
        if self.profiles[id] == None:
            profile = Profile()
            self.db.profile.loadById(profile,id)
            self.profiles[id]=profile
        return self.profiles[id]


    def show(self):
        print("inbox for " + self.profile.user)
        for id in ids:
            message=Message()
            self.db.message.loadById(message,id)
            display=(received and message.received != None) or (unreceived and message.received == None)
            if (display):
                sender=Profile()
                self.db.profile.loadById(sender,message.senderid)
                print("from: " + sender.user)
                print("sent: " + message.sent)
                print("dialog: " + message.dialog)

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
