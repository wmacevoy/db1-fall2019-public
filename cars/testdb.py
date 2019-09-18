#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import DB
from car import Car
from owner import Owner

class TestDB(TestCase):
    SCRATCH_DB_FILE="scratch.db"

    def testDefaultDB(self):
        db = DB()
        self.assertNotEqual(db.cursor(),None)
        db.connection.close()
    
    def testScratchDB(self):
        db = DB(TestDB.SCRATCH_DB_FILE)
        self.assertNotEqual(db.cursor(),None)
        db.connection.close()

    def getEmptyDB(self):
        db = DB(TestDB.SCRATCH_DB_FILE)
        if os.path.exists(db.dbFile):
            os.remove(db.dbFile)
        db.createTables()
        return db

    def getScratchDB(self):
        db = self.getEmptyScratchDB()

        alice = self.getAlice()
        bob = self.getBob()

        ford = self.getFord()
        nissan = self.getNissan()
        toyota = self.getToyota()

        db.owner.save(alice)
        db.owner.save(bob)

        ford.ownerId = alice.id
        nissan.ownerId = alice.id
        toyota.ownerId = bob.id

        db.car.save(ford)
        db.car.save(nissan)
        db.car.save(toyota)

        return db

    def getFord(self):
        ford = Car({'name': "mustang"})
        ford.addFuel(0.5)
        ford.start()
        ford.drive(250.0)
        return ford

    def getNissan(self):
        nissan = Car({'name':"rouge"})
        nissan.fuel = 0.75
        return nissan

    def getToyota(self):
        toyota = Car({'name':"tacoma"})
        return toyota
        
    def getAlice(self):
        alice = Owner({"name":"alice"})
        return alice
    
    def getBob(self):
        bob = Owner({"name":"bob"})
        return bob

    def testScratchIds(self):
        db=self.getScratchDB()
        ownerIds=db.owner.getIds()
        carIds=db.car.getIds()
        self.assertEqual(ownerIds,[1,2])
        self.assertEqual(carIds,[1,2,3])
        db.connection.commit()
        db.connection.close()


if __name__ == '__main__':
    main()
