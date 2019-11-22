class Message:
    def intOrNone(self, value):
        if value != None:
            return int(value)
        else:
            return None

    def strOrNone(self, value):
        if value != None:
            return str(value)
        else:
            return None

    DEFAULT_ID = None
    DEFAULT_RECIPIENTID = None
    DEFAULT_SENDERID = None
    DEFAULT_DIALOG = None
    DEFAULT_SENT = None
    DEFAULT_RECEIVED = None

    def __init__(self,memo={}):
        self._id = Message.DEFAULT_ID
        self._recipientid = Message.DEFAULT_RECIPIENTID
        self._senderid = Message.DEFAULT_SENDERID
        self._dialog = Message.DEFAULT_DIALOG
        self._sent = Message.DEFAULT_SENT
        self._received = Message.DEFAULT_RECEIVED
        self.update(memo)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = self.intOrNone(value)

    @property
    def recipientid(self):
        return self._recipientid
    @recipientid.setter
    def recipientid(self,value):
        self._recipientid = self.intOrNone(value)

    @property
    def senderid(self):
        return self._senderid
    @senderid.setter
    def senderid(self,value):
        self._senderid = self.intOrNone(value)

    @property
    def dialog(self):
        return self._dialog
    @dialog.setter
    def dialog(self,value):
        self._dialog = str(value)

    @property
    def sent(self):
        return self._sent
    @sent.setter
    def sent(self,value):
        self._sent = self.strOrNone(value)

    @property
    def received(self):
        return self._received
    @received.setter
    def received(self,value):
        self._received = self.strOrNone(value)

    @property
    def memo(self):
        return {'id': self._id,
                'recipientid': self._recipientid,
                'senderid': self._senderid,
                'dialog': self._dialog,
                'sent': self._sent,
                'received': self._received}

    def update(self,memo):
        if memo == None:
            return
        if 'id' in memo:
            self.id = memo['id']
        if 'recipientid' in memo:
            self.recipientid = memo['recipientid']
        if 'senderid' in memo:
            self.senderid = memo['senderid']
        if 'dialog' in memo:
            self.dialog = memo['dialog']
        if 'sent' in memo:
            self.sent = memo['sent']
        if 'received' in memo:
            self.received = memo['received']
    def __repr__(self):
        return "message (memo="+ repr(self.memo) + ")"
