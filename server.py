from flask import Flask, url_for, request, jsonify, abort, redirect, make_response
from OfficeDao import officeDao

app = Flask(__name__,static_url_path = '',static_folder = 'staticpages')

# root will just redirect to index.html static page
@app.route('/')
def home():
    return app.send_static_file('index.html')

# returns all staff in the database
@app.route('/staff')
def getAll():
    return jsonify(officeDao.getAll())

# returns all the costing rates in the database
@app.route('/costing')
def getAllCosting():
    return jsonify(officeDao.getAllCosting())

# returns the costing for a specific role
@app.route('/costing/<role>')
def findByRole(role):
    return jsonify(officeDao.findByRole(role))

# returns staff details for a specific staff member
@app.route('/staff/<int:staffID>')
def findById(staffID):
    return jsonify(officeDao.findById(staffID))

# creates a new staff member
@app.route('/staff', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    staff = {
        "staffID": request.json["staffID"],
        "name": request.json["name"],
        "role": request.json["role"],
        "expertise": request.json["expertise"],
        "availability": request.json["availability"]
    }
    return jsonify(officeDao.createStaff(staff))

# updates an existing staff member
@app.route('/staff/<int:staffID>', methods=['PUT'])
def update(staffID):
    foundStaff=officeDao.findById(staffID)
    print (foundStaff)
    if foundStaff == {}:
        return jsonify({}), 404
    currentStaff = foundStaff
    if 'name' in request.json:
        currentStaff['name'] = request.json['name']
    if 'role' in request.json:
        currentStaff['role'] = request.json['role']
    if 'expertise' in request.json:
        currentStaff['expertise'] = request.json['expertise']
    if 'availability' in request.json:
        currentStaff['availability'] = request.json['availability']
    officeDao.update(currentStaff)
    return jsonify(currentStaff)

# deletes a member of staff
@app.route('/staff/<int:staffID>', methods=['DELETE'])
def delete(staffID):
    officeDao.delete(staffID)
    return jsonify({"done": True})

#error handling
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

#error handling
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == "__main__":
    app.run(debug = True)