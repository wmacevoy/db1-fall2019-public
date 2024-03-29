import sqlite3 , os
from sqlite3 import Error

class MessageTable:
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
                sent text,
                received text
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
            columns.append('recipientid = ?')
            parameters.append(int(memo['recipientid']))
        if 'senderid' in memo:
            columns.append('senderid = ?')
            parameters.append(int(memo['senderid']))
        if 'dialog' in memo:
            columns.append('dialog = ?')
            parameters.append(str(memo['dialog']))
        if 'sent' in memo:
            columns.append('sent = ?')
            parameters.append(self.strOrNone(memo['sent']))
        if 'received' in memo:
            columns.append('received = ?')
            parameters.append(self.strOrNone(memo['received']))
        parameters.append(int(memo['id']))
        colstr = ",".join(columns)
        sql = "update message set " + colstr + "  where id = ?"
        cursor=self.cursor()
        cursor.execute(sql,parameters)

    def insert(self,memo):
        sql = "insert into message (recipientid, senderid, dialog, sent, received) values(?,?,?,?,?)"
        recipientid = int(memo['recipientid'])
        senderid = int(memo['senderid'])
        dialog = str(memo['dialog'])
        sent = self.strOrNone(memo['sent'])
        recieved = self.strOrNone(memo['received'])
        parameters = (recipientid,senderid,dialog,sent,recieved)
        cursor = self.cursor()
        cursor.execute(sql,parameters)
        return cursor.lastrowid

    def getIds(self):
        sql = "select (id) from message"
        cursor = self.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        ids = [None]*len(rows)
        for k in range(len(rows)):
            ids[k] = int(rows[k][0])
        return ids

    def getIdsBySenderid(self,senderid):
        sql = "select id from message where senderid=?"
        cursor = self.cursor()
        parameters=(int(senderid),)
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        ids = [None]*len(rows)
        for k in range(len(rows)):
            ids[k] = int(rows[k][0])
        return ids

    def getIdsByRecipientid(self,recipientid):
        sql = "select id from message where recipientid=?"
        cursor = self.cursor()
        parameters=(int(recipientid),)
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        ids = [None]*len(rows)
        for k in range(len(rows)):
            ids[k] = int(rows[k][0])
        return ids

    def deletebyId(self, id):
       sql = "delete from message where id = ?"
       parameters = (int(id))
       cursor = self.cursor()
       cursor.execute(sql, parameters)

    def strOrNone(self, value):
        if value == None:
            return None
        else:
            return str(value)

    def loadMemoById(self, id):
        sql = "select id,recipientid,senderid,dialog,received,sent from message where id=?"
        cursor = self.cursor()
        parameters = (int(id),)
        cursor.execute(sql,parameters)
        rows = cursor.fetchall()
        if len(rows)==0:
            return None
        else:
            row = rows[0]
            memo = {'id': int(row[0]),
                    'recipientid': int(row[1]),
                    'senderid': int(row[2]),
                    'dialog': str(row[3]),
                    'received': self.strOrNone(row[4]),
                    'sent': self.strOrNone(row[5])}
            return memo

    def loadById(self, message, id):
        memo = self.loadMemoById(id)
        message.update(memo)
