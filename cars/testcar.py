#!/usr/bin/env python

from unittest import TestCase, main

from car import Car

class TestCar(TestCase):

    def testDefaultCar(self):
        car = Car()
        self.assertEqual(car.id,Car.DEFAULT_ID)
        self.assertEqual(car.name,Car.DEFAULT_NAME)
        self.assertEqual(car.running,Car.DEFAULT_RUNNING)
        self.assertEqual(car.fuel,Car.DEFAULT_FUEL)

    def testCarId(self):
        testId=123
        car = Car()
        self.assertEqual(car.id,Car.DEFAULT_ID)
        car.id = testId
        self.assertEqual(car.id,testId)
        car.id = None
        self.assertEqual(car.id,None)

    def testCarName(self):
        testName = "not " + Car.DEFAULT_NAME
        car = Car()
        self.assertEqual(car.name,Car.DEFAULT_NAME)
        car.name = testName
        self.assertEqual(car.name,testName)

    def testCarRunning(self):
        testRunning=not Car.DEFAULT_RUNNING
        car = Car()
        self.assertEqual(car.running,Car.DEFAULT_RUNNING)
        car.running = testRunning
        self.assertEqual(car.running,testRunning)

    def testCarFuel(self):
        testFuel=1-Car.DEFAULT_FUEL
        car = Car()
        self.assertEqual(car.fuel,Car.DEFAULT_FUEL)
        car.fuel = testFuel
        self.assertEqual(car.fuel,testFuel)

    def defaultMemo(self):
        memo={'id':Car.DEFAULT_ID,
              'name':Car.DEFAULT_NAME,
              'running':Car.DEFAULT_RUNNING,
              'fuel':Car.DEFAULT_FUEL}
        return memo

    def assertCarMemoEqual(self,car,memo):
        carMemo=car.memo
        if 'id' in memo:
            self.assertEqual(car.id,memo['id'])
            self.assertEqual(carMemo['id'],memo['id'])
        if 'name' in memo:
            self.assertEqual(car.name,memo['name'])
            self.assertEqual(carMemo['name'],memo['name'])
        if 'running' in memo:
            self.assertEqual(car.running,memo['running'])
            self.assertEqual(carMemo['running'],memo['running'])
        if 'fuel' in memo:
            self.assertEqual(car.fuel,memo['fuel'])
            self.assertEqual(carMemo['fuel'],memo['fuel'])

    def testDefaultMemo(self):
        car = Car()
        expectedMemo = self.defaultMemo()
        self.assertCarMemoEqual(car,expectedMemo)

    def subtestInitMemo(self,memo):
        car = Car(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertCarMemoEqual(car,expectedMemo)

    def subtestUpdate(self,memo):
        car = Car()
        car.update(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertCarMemoEqual(car,expectedMemo)

    def subtestMemo(self,memo):
        self.subtestInitMemo(memo)
        self.subtestUpdate(memo)
        
    def testMemo(self):
        self.subtestMemo({'id':123})
        self.subtestMemo({'name':"not " + Car.DEFAULT_NAME})
        self.subtestMemo({'running': not Car.DEFAULT_RUNNING})
        self.subtestMemo({'fuel':1.0-Car.DEFAULT_FUEL})

if __name__ == '__main__':
    main()
