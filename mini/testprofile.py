#!/usr/bin/env python3

from unittest import TestCase, main

from profile import Profile

class TestProfile(TestCase):

    def testDefaultProfile(self):
        profile = Profile()
        self.assertEqual(profile.id,Profile.DEFAULT_ID)
        self.assertEqual(profile.user,Profile.DEFAULT_USER)
        self.assertEqual(profile.status,Profile.DEFAULT_STATUS)

    def testProfileId(self):
        testId=123
        profile = Profile()
        self.assertEqual(profile.id,Profile.DEFAULT_ID)
        profile.id = testId
        self.assertEqual(profile.id,testId)
        profile.id = None
        self.assertEqual(profile.id,None)

    def testProfileUser(self):
        testUser = "not " + str(Profile.DEFAULT_USER)
        profile = Profile()
        self.assertEqual(profile.user,Profile.DEFAULT_USER)
        profile.user = testUser
        self.assertEqual(profile.user,testUser)

    def testProfileStatus(self):
        testStatus=not Profile.DEFAULT_STATUS
        profile = Profile()
        self.assertEqual(profile.status,Profile.DEFAULT_STATUS)
        profile.status = testStatus
        self.assertEqual(profile.status,testStatus)

    def defaultMemo(self):
        memo={'id':Profile.DEFAULT_ID,
              'user':Profile.DEFAULT_USER,
              'status':Profile.DEFAULT_STATUS}
        return memo

    def assertProfileMemoEqual(self,profile,memo):
        profileMemo=profile.memo
        if 'id' in memo:
            self.assertEqual(profile.id,memo['id'])
            self.assertEqual(profileMemo['id'],memo['id'])
        if 'user' in memo:
            self.assertEqual(profile.user,memo['user'])
            self.assertEqual(profileMemo['user'],memo['user'])
        if 'status' in memo:
            self.assertEqual(profile.status,memo['status'])
            self.assertEqual(profileMemo['status'],memo['status'])


    def testDefaultMemo(self):
        profile = Profile()
        expectedMemo = self.defaultMemo()
        self.assertProfileMemoEqual(profile,expectedMemo)

    def subtestInitMemo(self,memo):
        profile = Profile(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertProfileMemoEqual(profile,expectedMemo)

    def subtestUpdate(self,memo):
        profile = Profile()
        profile.update(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertProfileMemoEqual(profile,expectedMemo)

    def subtestMemo(self,memo):
        self.subtestInitMemo(memo)
        self.subtestUpdate(memo)
    def testMemo(self):
        self.subtestMemo({'id':123})
        self.subtestMemo({'user':"not " + str(Profile.DEFAULT_USER)})
        self.subtestMemo({'status': not Profile.DEFAULT_STATUS})

if __name__ == '__main__':
    main()