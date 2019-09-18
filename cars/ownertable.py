import sqlite3
from sqlite3 import Error

class OwnerTable:
    def __init__(self,db):
        self._db = db

    def cursor(self):
        return self._db.cursor()

    def createTable(self):
        sql = """
            create table if not exists owner (
                id integer primary key,
                name text not null
            )
        """
        self.cursor().execute(sql)

    def save(self,owner):
        if owner.id != None:
            self.update(owner.memo)
        else:
            memo = owner.memo
            id=self.insert(memo)
            owner.id = id

    def insert(self,memo):
        sql = "insert into owner (name) values (?)"
        name = str(memo['name'])
        parameters = (name,)
        cursor=self.cursor()
        cursor.execute(sql,parameters)
        return cursor.lastrowid

    def update(self,memo):
        if memo == None:
            return
        columns =[]
        parameters = []
        if 'name' in memo:
            columns.append('name=?')
            parameters.append(str(memo['name']))
        parameters.append(int(memo['id']))
        colstr = ",".join(columns)
        sql = "update owner set " + colstr + "  where id=?"
        cursor=self.cursor()
        cursor.execute(sql,parameters)

    def loadMemoById(self,id):
        sql = "select id, name from owner where id=?"
        cursor=self.cursor()
        parameters=(int(id),)
        cursor.execute(sql,parameters)
        rows=cursor.fetchall()
        if len(rows)==0: 
            return None
        else:
            row=rows[0]
            memo = {'id':int(row[0]),
                    'name':str(row[1])}
            return memo

    def loadMemoByName(self,name):
        sql = "select id, name from owner where name=?"
        cursor=self.cursor()
        parameters=(str(name),)
        cursor.execute(sql,parameters)
        rows=cursor.fetchall()
        if len(rows)==0: 
            return None
        else:
            row=rows[0]
            memo = {'id':int(row[0]),
                    'name':str(row[1])}
            return memo

    def getIds(self):
        sql = "select (id) from owner"
        cursor = self.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        ids=[None]*len(rows)
        for k in range(len(rows)):
            ids[k]=int(rows[k][0])
        return ids

    def loadById(self,owner,id):
        memo=self.loadMemoById(id)
        owner.update(memo)

    def loadByName(self,owner,name):
        memo=self.loadMemoByName(name)
        owner.update(memo)
