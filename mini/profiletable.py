import sqlite3
from sqlite3 import Error
 
# dont need to put in the id
 
class ProfileTable:
   def __init__(self, db):
       self._db=db
 
   def cursor(self):
       return self._db.cursor()
 
   def createTable(self):
       sql = """
           create table if not exists profile(
               id integer primary key,
               user text not null,
               status integer not null
           )
       """
       self.cursor().execute(sql)
 
   def save(self, profile):
       if profile.id != None:
           self.update(profile.memo)
       else:
           memo = profile.memo
           id = self.insert(memo)
           profile.id = id
 
   def deleteById(self,id):
       sql = "delete from profile where id = ?"
       parameters = (int(id),)
       cursor = self.cursor()
       cursor.execute(sql,parameters)
 
   def deleteByName(self, user):
       sql = "delete from profile where user = ?"
       parameters = (str(user),)
       cursor = self.cursor()
       cursor.execute(sql,parameters)
 
   def insert(self, memo):
       sql = "insert into profile (user, status) values (?,?)"
      # id = int(memo['id'])
       user = str(memo['user'])
       status = bool(int(memo['status']))
       parameters = (user, status)
       cursor = self.cursor()
       cursor.execute(sql,parameters)
       return cursor.lastrowid
 
   def update(self, memo):
       if memo == None:
           return
       columns = []
       parameters = []
     #  if 'id' in memo:
       #    columns.append('id = ?')
        #   parameters.append(int(memo['id']))
       if 'user' in memo:
           columns.append('user = ?')
           parameters.append(str(memo['user']))
       if 'status' in memo:
           columns.append('status = ?')
           parameters.append(bool(int(memo['status'])))
       parameters.append(int(memo['id']))
       colstr = ",".join(columns)
       sql = "update profile set " + colstr + " where id = ?"
       cursor = self.cursor()
       cursor.execute(sql,parameters)

   def loadMemoById(self, id):
       sql = "select id, user, status from profile where id = ?"
       cursor = self.cursor()
       parameters = (int(id),)
       cursor.execute(sql, parameters)
       rows = cursor.fetchall()
       if len(rows)==0:
           return None
       else:
           row=rows[0]
           memo = {'id':int(row[0]),
                   'user':str(row[1]),
                   'status':bool(int(row[2]))}
           return memo
 
   def loadMemoByUser(self, user):
           sql = "select id, user, status from profile where user = ?"
           cursor = self.cursor()
           parameters = (str(user),)
           cursor.execute(sql, parameters)
           rows = cursor.fetchall()
           if len(rows) == 0:
               return None
           else:
               row = rows[0]
               memo = {'id':int(row[0]),
                   'user':str(row[1]),
                   'status':bool(int(row[2]))}
           return memo
 
   def getIds(self):
           sql = "select (id) from profile"
           cursor = self.cursor()
           cursor.execute(sql)
           rows = cursor.fetchall()
           ids = [None]*len(rows)
           for k in range(len(rows)):
               ids[k] = int(rows[k][0])
           return ids
 
   def loadById(self, profile, id):
           memo = self.loadMemoById(id)
           profile.update(memo)
 
   def loadByUser(self, profile, user):
           memo = self.loadMemoByUser(user)
           profile.update(memo)
 

