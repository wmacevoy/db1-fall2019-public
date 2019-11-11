#!/usr/bin/env python3

import os
from unittest import TestCase, main

from db import Db
from car import Car

from testdb import TestDb

class TestCarTable(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCarTable, self).__init__(*args, **kwargs)
        self._testDb = TestDb()

    @property
    def testDb(self):
        return self._testDb

    def testEmptyIds(self):
        db=self.testDb.getEmptyDb()
        ids=db.car.getIds()
        self.assertEqual(ids,[])
        db.connection.commit()
        db.connection.close()


    def testScratchIds(self):
        db=self.testDb.getScratchDb()
        ids=db.car.getIds()
        self.assertEqual(ids,[1,2,3])
        db.connection.commit()
        db.connection.close()

    def testSave(self):
        db=self.testDb.getEmptyDb()
        ford = self.testDb.getFord()
        nissan = self.testDb.getNissan()
        self.assertEqual(ford.id,None)
        self.assertEqual(nissan.id,None)
        db.car.save(ford)
        db.car.save(nissan)
        self.assertEqual(ford.id,1)
        self.assertEqual(nissan.id,2)
        db.connection.commit()
        db.connection.close()

    def testLoadFord(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getFord()
        expect.id = 1
        expect.ownerId = 1
        
        result = Car()
        db.car.loadByName(result, expect.name)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()


    def testLoadNissan(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getNissan()
        expect.id = 2
        expect.ownerId = 1        
        result = Car()
        db.car.loadByName(result, expect.name)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

    def testLoadToyota(self):
        db=self.testDb.getScratchDb()
        expect = self.testDb.getToyota()
        expect.id = 3
        expect.ownerId = 2        
        result = Car()
        db.car.loadByName(result, expect.name)
        self.assertEqual(expect.memo,result.memo)
        db.connection.commit()
        db.connection.close()

    def testUpdateFord(self):
        db=self.testDb.getScratchDb()
        ford = Car()
        db.car.loadByName(ford,self.testDb.getFord().name)
        ford.name = "classic " + ford.name
        ford.running = not ford.running
        ford.fuel = 0.75
        db.car.save(ford)
        car = Car()
        db.car.loadById(car,ford.id)
        self.assertEqual(car.memo,ford.memo)
        db.connection.commit()
        db.connection.close()

    def testDeleteFord(self):
        db=self.testDb.getScratchDb()
        ford = Car()
        name = self.testDb.getFord().name
        db.car.loadByName(ford,name)
        db.car.deleteById(ford.id)
        db.connection.commit()
        db.connection.close()

    def testUpdateNissan(self):
        db=self.testDb.getScratchDb()
        nissan = Car()
        db.car.loadByName(nissan,self.testDb.getNissan().name)
        nissan.name = "classic " + nissan.name
        nissan.running = not nissan.running
        nissan.fuel = 0.75
        db.car.save(nissan)
        car = Car()
        db.car.loadById(car,nissan.id)
        self.assertEqual(car.memo,nissan.memo)
        db.connection.commit()
        db.connection.close()


v