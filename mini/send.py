import sys,dbdatetime

from profile import Profile
from message import Message
from db import Db

class Sender:
    def __init__(self,senderUser, recipientUser, dialog):
        self.db = Db()
        self.sender=self.getOrCreateProfileByUser(user=senderUser,status=1)
        self.recipient=self.getOrCreateProfileByUser(user=recipientUser,status=None)
        self.dialog = dialog

    def getOrCreateProfileByUser(self,user,status):
        profile=Profile()
        self.db.profile.loadByUser(profile,user)
        if status != None:
            profile.status = status
        profile.user = user
        self.db.profile.save(profile)
        return profile

    def send(self):
        message = Message()
        message.senderid = self.sender.id
        message.recipientid = self.recipient.id
        message.dialog = self.dialog
        message.sent = dbdatetime.datetime.utcnow()
        message.received = None
        self.db.message.save(message)
        self.db.connection.commit()
        self.db.connection.close()

def send(senderUser, recipientUser, dialog):
    sender = Sender(senderUser,recipientUser,dialog)
    sender.send()

def testSend():
    send("alice","bob","testSend(" + str(dbdatetime.datetime.utcnow()) + ")")

def main():
    args = sys.argv
    args.pop(0)
    if len(args) == 0:
        testSend()
    else:
        send(*args)

if __name__ == '__main__':
    main()
