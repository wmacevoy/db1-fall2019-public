#!/usr/bin/env python

import os
from unittest import TestCase, main

from db import CarDB
from car import Car

class TestDB(TestCase):
    def testLogic(self):
        self.assertEqual(False,bool(int(0)))
        self.assertEqual(True,bool(int(1)))
        self.assertEqual(False,bool(int(False)))
        self.assertEqual(True,bool(int(True)))
        
    TEST_DB_FILE='TestCarDB.db'
    def getEmptyTestDB(self):
        if os.path.exists(TestDB.TEST_DB_FILE):
            os.remove(TestDB.TEST_DB_FILE)
        testDB = CarDB()
        testDB.dbFile=TestDB.TEST_DB_FILE
        testDB.createCarTable()
        return testDB

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
        
    def getBaseTestDB(self):
        db=self.getEmptyTestDB()
        db.insert(self.getFord().memo)
        db.insert(self.getNissan().memo)
        return db

    def testEmptyIds(self):
        db=self.getEmptyTestDB()
        ids=db.getIds()
        self.assertEqual(ids,[])
        db.connection.commit()
        db.connection.close()


    def testBaseIds(self):
        db=self.getBaseTestDB()
        ids=db.getIds()
        self.assertEqual(ids,[1,2])
        db.connection.commit()
        db.connection.close()

    def testSave(self):
        db=self.getEmptyTestDB()
        ford = self.getFord()
        nissan = self.getNissan()
        self.assertEqual(ford.id,None)
        self.assertEqual(nissan.id,None)
        db.save(ford)
        db.save(nissan)
        self.assertEqual(ford.id,1)
        self.assertEqual(nissan.id,2)
        db.connection.commit()
        db.connection.close()


    def testLoadFord(self):
        db=self.getBaseTestDB()
        unsavedFord = self.getFord()
        savedFord = Car()
        db.loadByName(savedFord,unsavedFord.name)
        self.assertNotEqual(savedFord.id,None)
        unsavedFord.id=savedFord.id
        self.assertEqual(unsavedFord.memo,savedFord.memo)
        db.connection.commit()
        db.connection.close()


    def testExample(self):
        db=self.getBaseTestDB()
        car = Car({'name': 'chevy', 'running': False})
        db.save(car)
        db.connection.commit()
        db.connection.close()

        
    def testLoadNissan(self):
        db=self.getBaseTestDB()
        unsavedNissan = self.getNissan()
        savedNissan = Car()
        db.loadByName(savedNissan,unsavedNissan.name)
        self.assertNotEqual(savedNissan.id,None)
        unsavedNissan.id=savedNissan.id
        self.assertEqual(unsavedNissan.memo,savedNissan.memo)
        db.connection.commit()
        db.connection.close()


    def testUpdateFord(self):
        db=self.getBaseTestDB()
        ford = Car()
        db.loadByName(ford,self.getFord().name)
        ford.name = "classic " + ford.name
        ford.running = not ford.running
        ford.fuel = 0.75
        db.save(ford)
        car = Car()
        db.loadById(car,ford.id)
        self.assertEqual(car.memo,ford.memo)
        db.connection.commit()
        db.connection.close()

    def testDeleteFord(self):
        db=self.getBaseTestDB() # ref db
        ford = Car() # blank car (all defaults)
        name = self.getFord().name # the name 'mustang'
        db.loadByName(ford,name)
        db.deleteById(ford.id)
        db.connection.commit()
        db.connection.close()
        print("done")

    def testUpdateNissan(self):
        db=self.getBaseTestDB()
        nissan = Car()
        db.loadByName(nissan,self.getNissan().name)
        nissan.name = "classic " + nissan.name
        nissan.running = not nissan.running
        nissan.fuel = 0.75
        db.save(nissan)
        car = Car()
        db.loadById(car,nissan.id)
        self.assertEqual(car.memo,nissan.memo)
        db.connection.commit()
        db.connection.close()


if __name__ == '__main__':
    main()
