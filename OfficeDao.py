#needed to connect to database
import mysql.connector
from mysql.connector import cursor
#allows authentication to the database without updating this file
import dbconfig as cfg

class OfficeDao:
    db=''
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    # function to create a new staff member
    def createStaff(self,staff):
        cursor = self.db.cursor()
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
        cursor.close()

    # function to create a new costing rate
    def createCosting(self,costing):
        cursor = self.db.cursor()
        sql="insert into costing (role, rate) values (%s, %s)"
        values = [
            costing['role'],
            costing['rate']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        cursor.close()

    # function to select a specific costing rate
    def findByRole(self,role):
        cursor = self.db.cursor()
        sql='select * from costing where role = %s'
        value = [str(role)]
        cursor.execute(sql,value)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictCosting(result)

    # converts the sql output from the staff table into dictionary format
    def convertToDict(self, result):
        colnames = ['staffID','name','role','expertise','availability']
        output={}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                output[colName] = value
        return output

    # function to return all staff members
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    # converts the sql output from the costing table into dictionary format
    def convertToDictCosting(self, result):
        colnames = ['role','rate']
        output={}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                output[colName] = value
        return output

    # function to return all costing rates
    def getAllCosting(self):
        cursor = self.db.cursor()
        sql = "select * from costing"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDictCosting(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    # function to select a specific staff member
    def findById(self, staffID):
        cursor = self.db.cursor()
        sql = 'select * from staff where staffID = %s'
        values = [ staffID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)
    
    # function to update an existing staff member
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
       cursor.close()
       return staff

    # function to delete a staff member
    def delete(self, staffID):
       cursor = self.db.cursor()
       sql = 'delete from staff where staffID = %s'
       values = [staffID]
       cursor.execute(sql, values)
       cursor.close()
       return {}

# this will allow the Dao to be imported to another python file
officeDao = OfficeDao()        