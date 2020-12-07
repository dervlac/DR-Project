import mysql.connector
from mysql.connector import cursor

class OfficeDao:
    db=''
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='datarepresentation'
        )
    
    def createStaff(self,staff):
        cursor=self.db.cursor()
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

    def createCosting(self,costing):
        cursor=self.db.cursor()
        sql="insert into costing (role, rate) values (%s, %s)"
        values = [
            costing['role'],
            costing['rate']
        ]
        cursor.execute(sql,values)
        self.db.commit()

    def convertToDict(self, result):
        colnames = ['staffID','name','role','expertise','availability']
        output={}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                output[colName] = value
        return output

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
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
        cursor = self.db.cursor()
        sql = "select * from costing"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDictCosting(result)
            returnArray.append(resultAsDict)
        return returnArray

    #add inner join for costing
    def findById(self, staffID):
        cursor = self.db.cursor()
        sql = 'select * from staff where staffID = %s'
        values = [ staffID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, staff):
       cursor = self.db.cursor()
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
       return staff

    def delete(self, staffID):
       cursor = self.db.cursor()
       sql = 'delete from staff where staffID = %s'
       values = [staffID]
       cursor.execute(sql, values)
       
       return {}

officeDao = OfficeDao()


        