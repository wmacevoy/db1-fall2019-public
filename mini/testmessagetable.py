#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import Db
from message import Message

from testdb import TestDb

class TestMessageTable(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMessageTable, self).__init__(*args, **kwargs)
        self._testDb = TestDb()

    @property
    def testDb(self):
        return self._testDb

    def testEmptyIds(self):
        db=self.testDb.getEmptyDb()
        ids=db.message.getIds()
        self.assertEqual(ids,[])
        db.connection.commit()
        db.connection.close()


    def testScratchIds(self):
        db=self.testDb.getScratchDb()
        ids=db.message.getIds()
        self.assertEqual(ids,[1,2,3,4])
        db.connection.commit()
        db.connection.close()

    def testSave(self):
        db=self.testDb.getEmptyDb()
        alice = self.testDb.getAlice()
        bob = self.testDb.getBob()
        db.profile.save(alice)
        db.profile.save(bob)
        hi = self.testDb.getHi(sender=alice,recipient=bob)
        lol = self.testDb.getLol(sender=bob,recipient=alice)
        self.assertEqual(hi.id,None)
        self.assertEqual(lol.id,None)
        db.message.save(hi)
        db.message.save(lol)
        self.assertEqual(hi.id,1)
        self.assertEqual(lol.id,2)
        db.connection.commit()
        db.connection.close()

    def testLoadHi(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getHi()
        expect.id = 1
        expect.senderid = 1
        expect.recipientid = 2
        
        result = Message()
        db.message.loadById(result, expect.id)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()


    def testLoadLol(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getLol()
        expect.id = 2
        expect.senderid = 2
        expect.recipientid = 3

        result = Message()
        db.message.loadById(result, expect.id)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

if __name__ == '__main__':
    main()
