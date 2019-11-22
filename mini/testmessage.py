#!/usr/bin/env python3

from unittest import TestCase, main
from message import Message
from dbdatetime import DbDateTime
import datetime
import calendar


class TestMessage(TestCase):

    def testDefaultMessage(self):
        message = Message()
        self.assertEqual(message.id, Message.DEFAULT_ID)
        self.assertEqual(message.recipientid, Message.DEFAULT_RECIPIENTID)
        self.assertEqual(message.senderid, Message.DEFAULT_SENDERID)
        self.assertEqual(message.dialog, Message.DEFAULT_DIALOG)
        self.assertEqual(message.sent, Message.DEFAULT_SENT)
        self.assertEqual(message.received, Message.DEFAULT_RECEIVED)

    def testMessageId(self):
        testId = 123

        message = Message()
        self.assertEqual(message.id, Message.DEFAULT_ID)
        message.id = testId
        self.assertEqual(message.id, testId)
        message.id = None
        self.assertEqual(message.id, None)

    def testRecipientId(self):
        testRecipientId = 1234
        message = Message()
        self.assertEqual(message.recipientid, Message.DEFAULT_RECIPIENTID)
        message.recipientid = testRecipientId
        self.assertEqual(message.recipientid, testRecipientId)
        message.recipientid = None
        self.assertEqual(message.recipientid, None)

    def testSenderId(self):
        testSenderId = 1234
        message = Message()
        self.assertEqual(message.recipientid, Message.DEFAULT_RECIPIENTID)
        message.senderid = testSenderId
        self.assertEqual(message.senderid, testSenderId)
        message.senderid = None
        self.assertEqual(message.senderid, None)

    def testMessageDialog(self):
        testDialog = "not " + str(Message.DEFAULT_DIALOG)
        message = Message()
        self.assertEqual(message.dialog, Message.DEFAULT_DIALOG)
        message.dialog = testDialog
        self.assertEqual(message.dialog, testDialog)

    def testMessageSent(self):
        testYear = 2020
        testMonth = 10
        testDay = 5
        testHour = 14
        testMinute = 30
        testSecond = 13
        testTimeTuple = (testYear, testMonth, testDay, testHour, testMinute, testSecond)
        testTimestamp = calendar.timegm(testTimeTuple)
        testTime = str(datetime.utcfromtimestamp(testTimestamp))

        message = Message()
        self.assertEqual(message.sent, Message.DEFAULT_SENT)
        message.sent = testTime
        self.assertEqual(message.sent, testTime)

    def testMessageReceived(self):
        testYear = 2020
        testMonth = 10
        testDay = 5
        testHour = 14
        testMinute = 30
        testSecond = 13
        testTimeTuple = (testYear, testMonth, testDay, testHour, testMinute, testSecond)
        testTimestamp = calendar.timegm(testTimeTuple)
        testTime = str(datetime.utcfromtimestamp(testTimestamp))

        message = Message()
        self.assertEqual(message.received, Message.DEFAULT_RECEIVED)
        message.received = testTime
        self.assertEqual(message.received, testTime)

    def defaultMemo(self):
        memo = {'id': Message.DEFAULT_ID,
                'recipientid': Message.DEFAULT_RECIPIENTID,
                'senderid': Message.DEFAULT_SENDERID,
                'dialog': Message.DEFAULT_DIALOG,
                'sent': Message.DEFAULT_SENT,
                'received': Message.DEFAULT_RECEIVED}
        return memo

    def assertMessageMemoEqual(self, message, memo):
        messageMemo = message.memo
        if 'id' in memo:
            self.assertEqual(message.id, memo['id'])
            self.assertEqual(messageMemo['id'], memo['id'])
        if 'senderid' in memo:
            self.assertEqual(message.senderid, memo['senderid'])
            self.assertEqual(messageMemo['senderid'], memo['senderid'])
        if 'recipientid' in memo:
            self.assertEqual(message.recipientid, memo['recipientid'])
            self.assertEqual(messageMemo['recipientid'], memo['recipientid'])
        if 'dialog' in memo:
            self.assertEqual(message.dialog, memo['dialog'])
            self.assertEqual(messageMemo['dialog'], memo['dialog'])
        if 'sent' in memo:
            self.assertEqual(message.sent, memo['sent'])
            self.assertEqual(messageMemo['sent'], memo['sent'])
        if 'received' in memo:
            self.assertEqual(message.received, memo['received'])
            self.assertEqual(messageMemo['received'], memo['received'])

    def testDefaultMemo(self):
        message = Message()
        expectedMemo = self.defaultMemo()
        self.assertMessageMemoEqual(message, expectedMemo)

    def subtestInitMemo(self, memo):
        message = Message(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertMessageMemoEqual(message, expectedMemo)

    def subtestUpdate(self, memo):
        message = Message()
        message.update(memo)
        expectedMemo = self.defaultMemo()
        expectedMemo.update(memo)
        self.assertMessageMemoEqual(message, expectedMemo)

    def subtestMemo(self, memo):
        self.subtestInitMemo(memo)
        self.subtestUpdate(memo)

    def testMemo(self):
        self.subtestMemo({'id': 123})
        self.subtestMemo({'senderid': 123})
        self.subtestMemo({'recipientid': 123})
        self.subtestMemo({'dialog': 'not ' + str(Message.DEFAULT_DIALOG)})
        self.subtestMemo({'sent': '1970-01-02 08:30:47'})
        self.subtestMemo({'received': '2020-02-01 14:13:50'})


if __name__ == '__main__':
    main()
