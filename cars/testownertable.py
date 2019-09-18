#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import Db
from owner import Owner

from testdb import TestDb

class TestOwnerTable(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOwnerTable, self).__init__(*args, **kwargs)
        self._testDb = TestDb()

    @property
    def testDb(self):
        return self._testDb

    def testEmptyIds(self):
        db=self.testDb.getEmptyDb()
        ids=db.owner.getIds()
        self.assertEqual(ids,[])
        db.connection.commit()
        db.connection.close()


    def testScratchIds(self):
        db=self.testDb.getScratchDb()
        ids=db.owner.getIds()
        self.assertEqual(ids,[1,2])
        db.connection.commit()
        db.connection.close()

    def testSave(self):
        db=self.testDb.getEmptyDb()
        alice = self.testDb.getAlice()
        bob = self.testDb.getBob()
        self.assertEqual(alice.id,None)
        self.assertEqual(bob.id,None)
        db.owner.save(alice)
        db.owner.save(bob)
        self.assertEqual(alice.id,1)
        self.assertEqual(bob.id,2)
        db.connection.commit()
        db.connection.close()

    def testLoadAlice(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getAlice()
        expect.id = 1
        
        result = Owner()
        db.owner.loadByName(result, expect.name)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()


    def testLoadBob(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getBob()
        expect.id = 2
        result = Owner()
        db.owner.loadByName(result, expect.name)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

    def testUpdateAlice(self):
        db=self.testDb.getScratchDb()
        alice = Owner()
        db.owner.loadByName(alice,self.testDb.getAlice().name)
        alice.name = "allison"
        db.owner.save(alice)
        owner = Owner()
        db.owner.loadById(owner,alice.id)
        self.assertEqual(owner.memo,alice.memo)
        db.connection.commit()
        db.connection.close()

    def testDeleteAlice(self):
        db=self.testDb.getScratchDb()
        alice = Owner()
        name = self.testDb.getAlice().name
        db.owner.loadByName(alice,name)
        db.owner.deleteById(alice.id)
        db.connection.commit()
        db.connection.close()

if __name__ == '__main__':
    main()
