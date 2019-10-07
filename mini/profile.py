class Profile:
   DEFAULT_ID = None
   DEFAULT_USER = "unkown"
   DEFAULT_STATUS = False
 
   MAX_RANGE = 1.0
   def __init__(self, memo = {}):
       self.id = Profile.DEFAULT_ID
       self.user = Profile.DEFAULT_USER
       self.status = Profile.DEFAULT_STATUS
       self.update(memo)
 
   @property
   def id(self):
       return self._id
 
   @id.setter
   def id(self, value):
       if value == None:
           self._id = None
       else:
           self._id = int(value)
 
   @property
   def user(self):
       return self.user
 
   @user.setter
   def user(self, value):
       self._user = srt(value)
 
   @property
   def status(self):
       return self.status
 
   @status.setter
   def status(self, value):
       self._status = bool(int(value))
 
   @property
   def memo(self):
       return {'id': self._id,
               'user': self._user,
               'status': self._status}
 
   def update(self, memo):
       if memo == None:
           return
       if 'id' in memo:
           self.id = memo['id']
       if 'user' in memo:
           self.user = memo['user']
       if 'status' in memo:
           self.status = memo['status']
 
   def statusOn(self):
       self._status = True
  
   def statusOff(self):
       self._status = False
 
   def __repr__(self):
       return "profile(memo =" +repr(self.memo) + ")"
      

