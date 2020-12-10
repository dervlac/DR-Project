import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class OfficeDao:
    db=''
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self):
        db=self.connectToDB() 
        db.close()
    
    def createStaff(self,staff):
        db = self.getConnection()
        cursor = db.cursor()
        sql="insert into staff (staffID, name, role, expertise, availability) values (%s, %s, %s, %s, %s)"
        values = [
            staff['staffID'],
            staff['name'],
            staff['role'],
            staff['expertise'],
            staff['availability'],
        ]
        cursor.execute(sql,values)
        self.db.commit()
        db.close()

    def createCosting(self,costing):
        db = self.getConnection()
        cursor = db.cursor()
        sql="insert into costing (role, rate) values (%s, %s)"
        values = [
            costing['role'],
            costing['rate']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        db.close()

    def findByRole(self,role):
        db = self.getConnection()
        cursor = db.cursor()
        sql='select * from costing where role = %s'
        value = [str(role)]
        cursor.execute(sql,value)
        result = cursor.fetchone()
        db.close()
        return self.convertToDictCosting(result)

    def convertToDict(self, result):
        colnames = ['staffID','name','role','expertise','availability']
        output={}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                output[colName] = value
        return output


    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    def convertToDictCosting(self, result):
        colnames = ['role','rate']
        output={}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                output[colName] = value
        return output

    def getAllCosting(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from costing"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDictCosting(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    def findById(self, staffID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from staff where staffID = %s'
        values = [ staffID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        db.close()
        return self.convertToDict(result)

    def update(self, staff):
       db = self.getConnection()
       cursor = db.cursor()
       sql = "update staff set name = %s, role = %s, expertise = %s, availability = %s where staffID = %s"
       values = [
           staff['name'],
           staff['role'],
           staff['expertise'],
           staff['availability'],
           staff['staffID']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       db.close()
       return staff

    def delete(self, staffID):
       db = self.getConnection()
       cursor = db.cursor()
       sql = 'delete from staff where staffID = %s'
       values = [staffID]
       cursor.execute(sql, values)
       db.close()
       return {}

officeDao = OfficeDao()


        