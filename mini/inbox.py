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
        print("profile=" + str(self.profile))
        sql = """select recipient.user,message.sent,message.received
from message join profile recipient on recipient.id = message.recipientid
where recipientid = ?"""
        parameters=(self.profile.id,)
        cursor=self.db.cursor()
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        info = [None]*len(rows)
        for k in range(len(rows)):
            info[k] = {'from': rows[k][0], 'sent':rows[k][1], 'read':rows[k][2]}
        print(repr(info))
        # "from" / when sent / read/unread

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
