class Owner:
    DEFAULT_ID=None
    DEFAULT_NAME="unknown"
    def __init__(self,memo={}): # constructor
        self._id = Owner.DEFAULT_ID
        self._name = Owner.DEFAULT_NAME
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
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=str(value)

    @property
    def memo(self):
        return {'id': self._id,
                'name': self._name}

    def update(self,memo):
        if memo == None: 
            return
        if 'id' in memo:
            self.id = memo['id']
        if 'name' in memo:
            self.name = memo['name']
    def __repr__(self):
        return "Owner(memo=" + repr(self.memo) + ")"
