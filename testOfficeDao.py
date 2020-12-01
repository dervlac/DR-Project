#testOfficeDao

from OfficeDao import officeDao

cost1 = {
    'role':'Analyst',
    'rate':50
}
cost2 = {
    'role':'Senior Analyst',
    'rate':100
}
cost3 = {
    'role':'Manager',
    'rate':150
}
cost4 = {
    'role':'Director',
    'rate':200
}

staff1 = {
    'staffID':101,
    'name':'Mary Burke',
    'role' : 'Analyst',
    'expertise':'Accounting',
    'availability':15
}
staff2 = {
    'staffID':102,
    'name':'John Murphy',
    'role':"Senior Analyst",
    'expertise':'Finance',
    'availability':20
}
staff3 = {
    'staffID':103,
    'name':'Sarah Kelly',
    'role':"Manager",
    'expertise':'IT',
    'availability':27
}
staff4 = {
    'staffID':104,
    'name':'Mark Harris',
    'role':"Manager",
    'expertise':'Cyber Security',
    'availability':10
}
staff5 = {
    'staffID':105,
    'name':'Rachel Keating',
    'role':"Director",
    'expertise':'Tax',
    'availability':12
}

#officeDao.createCosting(cost1)
#officeDao.createCosting(cost2)
#officeDao.createCosting(cost3)
#officeDao.createCosting(cost4)

#officeDao.createStaff(staff1)
#officeDao.createStaff(staff2)
#officeDao.createStaff(staff3)
#officeDao.createStaff(staff4)
#officeDao.createStaff(staff5)


returnvalue = officeDao.getAll()
print(returnvalue)