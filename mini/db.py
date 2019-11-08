import sqlite3, os
from sqlite3 import Error
from profiletable import ProfileTable
from messagetable import MessageTable
from os import path


class Db:
    DEFAULT_DB_FILE = str(os.path.expanduser("~/mini.db"))

    def __init__(self, dbFile=DEFAULT_DB_FILE):
        self._connection = None
        self._profile = ProfileTable(self)
        self._messgae = MessageTable(self)
        self._dbFile = None
        self._dbFile = dbFile

    @property
    def profile(self):
        return self._profile

    @property
    def message(self):
        return self._messgae

    @property
    def dbFile(self):
        return self._dbFile

    @dbFile.setter
    def dbFile(self, value):
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
            self.createTables()
        return self._connection

    def cursor(self):
        return self.connection.cursor()

    def createTables(self):
        self.profile.createTable()
        self.message.createTable()

