import sqlite3
from sqlite3 import Error

class CarDB:
    def __init__(self):
        self._connection = None
        self._dbFile = "CarDB.db"
    
    @property
    def dbFile(self):
        return self._dbFile

    @dbFile.setter
    def dbFile(self,value):
        if self._connection != None:
            raise ValueError('connection is already open.')
        self._dbFile=value

    @property
    def connection(self):
        if self._connection == None:
            self._connection = sqlite3.connect(self._dbFile)
        return self._connection

    def cursor(self):
        return self.connection.cursor()

    def createCarTable(self):
        sql = """
            create table if not exists car (
                id integer primary key,
                name text not null,
                running integer not null,
                fuel real not null
            )
        """
        self.cursor().execute(sql)

    def save(self,car):
        if car.id != None:
            self.update(car.memo)
        else:
            memo = car.memo
            id=self.insert(memo)
            car.id = id

    def insert(self,memo):
        sql = "insert into car (name,running,fuel) values (?,?,?)"
        name = str(memo['name'])
        running = bool(int(memo['running']))
        fuel = float(memo['fuel'])
        parameters = (name,running,fuel)
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
        if 'running' in memo:
            columns.append('running=?')
            parameters.append(bool(int(memo['running'])))
        if 'fuel' in memo:
            columns.append('fuel=?')
            parameters.append(float(memo['fuel']))
        parameters.append(int(memo['id']))
        colstr = ",".join(columns)
        sql = "update car set " + colstr + "  where id=?"
        cursor=self.cursor()
        cursor.execute(sql,parameters)

    def loadMemoById(self,id):
        sql = "select id, name, fuel, running from car where id=?"
        cursor=self.cursor()
        parameters=(int(id),)
        cursor.execute(sql,parameters)
        rows=cursor.fetchall()
        if len(rows)==0: 
            return None
        else:
            row=rows[0]
            memo = {'id':int(row[0]),
                    'name':str(row[1]),
                    'fuel':float(row[2]),
                    'running':bool(int(row[3]))}
            return memo

    def loadMemoByName(self,name):
        sql = "select id, name, fuel, running from car where name=?"
        cursor=self.cursor()
        parameters=(str(name),)
        cursor.execute(sql,parameters)
        rows=cursor.fetchall()
        if len(rows)==0: 
            return None
        else:
            row=rows[0]
            memo = {'id':int(row[0]),
                    'name':str(row[1]),
                    'fuel':float(row[2]),
                    'running':bool(int(row[3])) }
            return memo

    def getIds(self):
        sql = "select (id) from car";
        cursor = self.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        ids=[None]*len(rows)
        for k in range(len(rows)):
            ids[k]=int(rows[k][0])
        return ids

    def loadById(self,car,id):
        memo=self.loadMemoById(id)
        car.update(memo)

    def loadByName(self,car,name):
        memo=self.loadMemoByName(name)
        car.update(memo)