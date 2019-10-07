import sqlite3 , os
from sqlite3 import Error
 
class Messagetable:
    def __init__(self,db):
        self._db = db
    def cursor(self):
        return self._db.cursor()
    def createTable(self):
        sql = """
            create table if not exists message (
                id integer primary key,
                recipientid integer not null,
                senderid integer not null,
                dialog text not null,
                sent integer not null,
                received integer not null
            )
        """
        self.cursor().execute(sql)
    
    def save(self,message):
        if message.id != None:
            self.update(message.memo)
        else:
            memo = message.memo
            id = self.insert(memo)
            message.id = id
 
 
    def update(self, memo):
        if memo == None:
            return
        columns =[]
        parameters = []
        if 'recipientid' in memo:
            columns.append('recipientid=?')
            parameters.append(int(memo['recipientid']))
        if 'senderid' in memo:
            columns.append('senderid=?')
            parameters.append(int(memo['senderid']))
        if 'dialog' in memo:
            columns.append('dialog=?')
            parameters.append(str(memo['dialog']))
        if 'sent' in memo:
            columns.append('sent=?')
            parameters.append(int(memo['sent']))
        if 'recevied' in memo:
            columns.append('recevied=?')
            parameters.append(int(memo['recevied']))
        parameters.append(int(memo['id']))
        colstr = ",".join(columns)
        sql = "update message set " + colstr + "  where id=?"
        cursor=self.cursor()
        cursor.execute(sql,parameters)
 
    def insert(self,memo):
        sql = "insert into message (recipientid) values(?)"
        recipientid = int(memo['recipientid'])
        parameters = (recipientid,)
        cursor = self.cursor()
        cursor.execute(sql,parameters)
        return cursor.lastrowid
 
    def loadbyName(self, message, name):
       memo = self.loadMemoByName(name)
       message.update(memo)
 
    def loadbyStatus(self, message, status):
       memo = self.loadMemoByStatus(status)
       message.update(memo)
 
    def getIds(self):
       sql = "select (id) from message"
       cursor = self.cursor()
       cursor.execute(sql)
       rows = cursor.fetchall()
       ids = [None]*len(rows)
       for k in range(len(rows)):
           ids[k] = int(rows[k][0])
       return ids
 
    def deletebyId(self, id):
       sql = "delete from owner where id = ?"
       parameters = (int(id))
       cursor = self.cursor()
       cursor.execute(sql, parameters)
 
    def loadMemoByID(self,id):
        sql = "select id from message where id=?"
        cursor = self.cursor()
        parameters = (int(id),)
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        if len(rows)==0:
            return None
        else:
            row = rows[0]
            memo = {'id': int(row[0])}
            return memo
 
    def loadMemoByRecipientID(self,recipientid):
        sql = "select id, recipientid from message where recipientid=?"
        cursor=self.cursor()
        parameters=(int(recipientid),)
        cursor.execute(sql,parameters)
        rows=cursor.fetchall()
        if len(rows)==0: 
            return None
        else:
            row=rows[0]
            memo = {'id':int(row[0]),
                    'recipientid':int(row[1])}
            return memo
 
    def loadbyID(self, message, id):
        memo = self.loadMemoByID(id)
        message.update(memo)
    def loadbyRecipientID(self,message,recipientid):
        memo=self.loadMemoByRecipientID(recipientid)
        message.update(memo)
 

