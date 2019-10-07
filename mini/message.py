class Message:
    DEFAULT_ID = None
    DEFAULT_RECIPIENTID = None
    DEFAULT_SENDERID = None
    DEFAULT_DIALOG = "Empty"
    DEFAULT_SENT = None
    DEFAULT_RECEIVED = None
 
    def __init__(self,memo={}):
        self._id = DEFAULT_ID
        self._recipientid = DEFAULT_RECIPIENTID
        self._senderid = DEFAULT_SENDERID
        self._dialog = DEFAULT_DIALOG
        self._sent = DEFAULT_SENT
        self._received = DEFAULT_RECEIVED
        self.update(memo)
 
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        if value == None:
            self._id = None
        else:
            self._id = int(value)
 
    @property
    def recipientid(self):
        return self._recipientid
    @recipientid.setter
    def recipientid(self,value):
        if value == None:
            self._recipientid = None
        else:
            self._recipientid = int(value)
    @property
    def senderid(self):
        return self._senderid
    @senderid.setter
    def senderid(self,value):
        if value == None:
            self._senderid = None
        else:
            self._senderid = int(value)  
    @property
    def dialog(self):
        return self._dialog
    @message.setter
    def dialog(self,value):
        self._dialog = str(value)
    @property
    def sent(self):
        return self._sent
    @sent.setter
    def sent(self,value):
        if value == None:
            self._sent = None
        else:
            self._sent = int(value)
    @property
    def received(self):
        return self._received
    @received.setter
    def received(self,value):
        if value == None:
            self._received = None
        else:
            self._received = int(value)
 
    @property
    def memo(self):
        return {}
 
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
        if 'receved' in memo:
            self.received = memo['received']
    def __repr__(self):
        return "message (memo="+ repr(self.memo) + ")"
    

