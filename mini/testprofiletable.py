#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import Db
from profile import Profile

from testdb import TestDb

class TestProfileTable(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProfileTable, self).__init__(*args, **kwargs)
        self._testDb = TestDb()

    @property
    def testDb(self):
        return self._testDb

    def testEmptyIds(self):
        db=self.testDb.getEmptyDb()
        ids=db.profile.getIds()
        self.assertEqual(ids,[])
        db.connection.commit()
        db.connection.close()

    def testScratchIds(self):
        db=self.testDb.getScratchDb()
        ids=db.profile.getIds()
        self.assertEqual(ids,[1,2,3])
        db.connection.commit()
        db.connection.close()

    def testSave(self):
        db=self.testDb.getEmptyDb()
        alice = self.testDb.getAlice()
        bob = self.testDb.getBob()
        cindy = self.testDb.getCindy()
        self.assertEqual(alice.id,None)
        self.assertEqual(bob.id,None)
        self.assertEqual(cindy.id,None)
        db.profile.save(alice)
        db.profile.save(bob)
        db.profile.save(cindy)
        self.assertEqual(alice.id,1)
        self.assertEqual(bob.id,2)
        self.assertEqual(cindy.id,3)
        db.connection.commit()
        db.connection.close()

    def testLoadAlice(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getAlice()
        expect.id = 1
        
        result = Profile()
        db.profile.loadByUser(result, expect.user)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()


    def testLoadBob(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getBob()
        expect.id = 2
        result = Profile()
        db.profile.loadByUser(result, expect.user)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

    def testLoadCindy(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getCindy()
        expect.id = 3
        result = Profile()
        db.profile.loadByUser(result, expect.user)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

    def testUpdateAlice(self):
        db=self.testDb.getScratchDb()
        alice = Profile()
        db.profile.loadByUser(alice,self.testDb.getAlice().user)
        alice.status = not alice.status
        db.profile.save(alice)
        profile = Profile()
        db.profile.loadById(profile,alice.id)
        self.assertEqual(profile.memo,alice.memo)
        db.connection.commit()
        db.connection.close()

    def testDeleteAlice(self):
        db=self.testDb.getScratchDb()
        alice = Profile()
        name = self.testDb.getAlice().user
        db.profile.loadByUser(alice,name)
        db.profile.deleteById(alice.id)
        db.connection.commit()
        db.connection.close()

if __name__ == '__main__':
    main()