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
        sql = """select sender.user,message.sent,message.received,message.id
from message join profile sender on sender.id = message.senderid
where recipientid = ?"""
        parameters=(self.profile.id,)
        cursor=self.db.cursor()
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        info = [None]*len(rows)
        for k in range(len(rows)):
            info[k] = {'from': rows[k][0], 'sent':rows[k][1], 'read':rows[k][2], 'messageid': rows[k][3]}
        for message in info:
            msgfrom=message['from']
            msgsent=message['sent']
            msgread=message['read']
            msgid=message['messageid']
            if msgread != None:
                print(f"{msgid}: from {msgfrom} sent on {msgsent} read on {msgread}")
            else:
                print(f"{msgid}: from {msgfrom} sent on {msgsent} unread")
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
