#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import Db
from profile import Profile
from message import Message

class TestDb(TestCase):
    SCRATCH_DB_FILE="scratch.db"

    def testDefaultDb(self):
        db = Db()
        self.assertNotEqual(db.cursor(),None)
        db.connection.close()
    
    def testScratchDb(self):
        db = Db(TestDb.SCRATCH_DB_FILE)
        self.assertNotEqual(db.cursor(),None)
        db.connection.close()

    def getEmptyDb(self):
        db = Db(TestDb.SCRATCH_DB_FILE)
        if os.path.exists(db.dbFile):
            os.remove(db.dbFile)
        db.createTables()
        return db

    def getScratchDb(self):
        db = self.getEmptyDb()

        alice = self.getAlice()
        bob = self.getBob()
        cindy = self.getCindy()

        db.profile.save(alice)
        db.profile.save(bob)
        db.profile.save(cindy)

        hi = self.getHi(sender=alice,recipient=bob)
        lol = self.getLol(sender=bob,recipient=cindy)
        sup = self.getSup(sender=alice,recipient=cindy)
        wave = self.getWave(sender=bob,recipient=alice)

        db.message.save(hi)
        db.message.save(lol)
        db.message.save(sup)
        db.message.save(wave)
        return db

    def getAlice(self):
        profile = Profile({"user":"alice", "status": True})
        return profile
    
    def getBob(self):
        profile = Profile({"user":"bob", "status": False})
        return profile

    def getCindy(self):
        profile = Profile({"user":"cindy", "status": True})
        return profile

    def idOrNone(self,profile):
        if profile == None:
            return None
        else:
            return profile.id
        
    def getHi(self,sender=None,recipient=None):
        message = Message({'recipientid':self.idOrNone(recipient),
                           'senderid':self.idOrNone(sender),
                           'dialog':"Hi!",
                           'sent': "2019-10-02 09:30:45",
                           'recieved': "2019-10-02 10:30:45"})
        return message

    def getLol(self,sender,recipient):
        message = Message({'recipientid':self.idOrNone(recipient),
                           'senderid':self.idOrNone(sender),
                           'dialog':"Lol! \u1F923",
                           'sent': None,
                           'recieved': None})
        return message

    def getSup(self,sender,recipient):
        message = Message({'recipientid':self.idOrNone(recipient),
                           'senderid':self.idOrNone(sender),
                           'dialog':"Sup?",
                           'sent': None,
                           'recieved': None})
        return message
        
    def getWave(self,sender,recipient):
        message = Message({'recipientid':self.idOrNone(recipient),
                           'senderid':self.idOrNone(sender),
                           'dialog':"\u1F44B",
                           'sent': None,
                           'recieved': None})
        return message
        
    def testScratchIds(self):
        db=self.getScratchDb()
        messageIds=db.message.getIds()
        profileIds=db.profile.getIds()
        self.assertEqual(messageIds,[1,2,3,4])
        self.assertEqual(profileIds,[1,2,3])
        db.connection.commit()
        db.connection.close()


if __name__ == '__main__':
    main()
