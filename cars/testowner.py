#!/usr/bin/env python3

from unittest import TestCase, main

from owner import Owner

class TestOwner(TestCase):

    def testDefaultOwner(self):
        owner = Owner()
        self.assertEqual(owner.id,Owner.DEFAULT_ID)
        self.assertEqual(owner.name,Owner.DEFAULT_NAME)

    def testOwnerId(self):
        testId=123
        owner = Owner()
        self.assertEqual(owner.id,Owner.DEFAULT_ID)
        owner.id = testId
        self.assertEqual(owner.id,testId)
        owner.id = None
        self.assertEqual(owner.id,None)

    def testOwnerName(self):
        testName = "not " + Owner.DEFAULT_NAME
        owner = Owner()
        self.assertEqual(owner.name,Owner.DEFAULT_NAME)
        owner.name = testName
        self.assertEqual(owner.name,testName)

    def defaultMemo(self):
        memo={'id':Owner.DEFAULT_ID,
              'name':Owner.DEFAULT_NAME}
        return memo

    def assertOwnerMemoEqual(self,owner,memo):
        ownerMemo=owner.memo
        if 'id' in memo:
            self.assertEqual(owner.id,memo['id'])
            self.assertEqual(ownerMemo['id'],memo['id'])
        if 'name' in memo:
            self.assertEqual(owner.name,memo['name'])
            self.assertEqual(ownerMemo['name'],memo['name'])

    def testDefaultMemo(self):
        owner = Owner()
        expectedMemo = self.defaultMemo()
        self.assertOwnerMemoEqual(owner,expectedMemo)

    def subtestInitMemo(self,memo):
        owner = Owner(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertOwnerMemoEqual(owner,expectedMemo)

    def subtestUpdate(self,memo):
        owner = Owner()
        owner.update(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertOwnerMemoEqual(owner,expectedMemo)

    def subtestMemo(self,memo):
        self.subtestInitMemo(memo)
        self.subtestUpdate(memo)

    def testMemo(self):
        self.subtestMemo({'id':123})
        self.subtestMemo({'name':"not " + Owner.DEFAULT_NAME})

if __name__ == '__main__':
    main()
