import sqlite3, os
from sqlite3 import Error
from cartable import CarTable
from ownertable import OwnerTable

class DB:
    DEFAULT_DB_FILE="fleet.db"

    def __init__(self, dbFile = DEFAULT_DB_FILE):
        self._connection = None
        self._owner = OwnerTable(self)
        self._car = CarTable(self)
        self._dbFile = None
        self.dbFile = dbFile
    
    @property
    def car(self):
        return self._car
    @property
    def owner(self):
        return self._owner

    @property
    def dbFile(self):
        return self._dbFile

    @dbFile.setter
    def dbFile(self,value):
        if self._connection != None:
            raise ValueError('connection is already open.')

        if value.startswith(".") or value.startswith("/"):
            self._dbFile = value
        else:
            dir = os.path.dirname(os.path.realpath(__file__))
            self._dbFile = dir + "/" + value

    @property
    def connection(self):
        if self._connection == None:
            self._connection = sqlite3.connect(self._dbFile)
        return self._connection

    def cursor(self):
        return self.connection.cursor()

    def createTables(self):
        self.car.createTable()
        self.owner.createTable()
