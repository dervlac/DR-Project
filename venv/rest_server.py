from flask import Flask, url_for, request, jsonify, abort, redirect


app = Flask(__name__,static_url_path = '',static_folder = 'staticpages')

bookshop = [
    {"id":1, "Title":"Game of Thrones", "Author":"George R. R. Martin", "Price":14.99, "Stock":100},
    {"id":2, "Title":"Normal People", "Author":"Sally Rooney", "Price":10.99, "Stock":35},
    {"id":3, "Title":"1984", "Author":"George Orwell", "Price":7.99, "Stock":150},
    {"id":4, "Title":"The Poppy War", "Author":"R.F. Kuang", "Price":10.99, "Stock":50},
    {"id":5, "Title":"Cook, Eat Repeat", "Author":"Nigella Lawson", "Price":25.00, "Stock":20},
]

nextID = 6

@app.route('/')
def index():
    return "Hello World!"

@app.route('/login')
def login():
    return "This page will be the login page"

@app.route('/bookshop')
def getAll():
    return jsonify(bookshop)

@app.route('/bookshop/<int:id>')
def getBookByID(id):
    found_books = list(filter(lambda t: t["id"] == id, bookshop))
    if len(found_books) == 0:
        return jsonify({}), 204
    return jsonify(found_books[0])

# curl -X POST -H "content-type":"application/json" -d "{\"Title\":\"Northern Lights\", \"Author\":\"Phillip Pullman\", \"Price\":9.99, \"Stock\":75}" http://127.0.0.1:5000/bookshop
@app.route('/bookshop', methods=['POST'])
def stock_bookshop():
    global nextID
    if not request.json:
        abort(400)
    new_book = {"id":nextID, "Title":request.json["Title"], "Author":request.json["Author"], "Price":request.json["Price"], "Stock":request.json["Stock"]}
    bookshop.append(new_book)
    nextID += 1
    return jsonify(new_book)

@app.route('/bookshop/<int:id>', methods = ['PUT'])
def update_stock(id):
    found_books = list(filter(lambda t: t["id"] == id, bookshop))
    if len(found_books) == 0:
        return jsonify({}), 404
    current_book = found_books[0]
    if "Title" in request.json:
        current_book["Title"] = request.json["Title"]
    if "Author" in request.json:
        current_book["Author"] = request.json["Author"]
    if "Price" in request.json:
        current_book["Price"] = request.json["Price"]
    if "Stock" in request.json:
        current_book["Stock"] = request.json["Stock"]
    return "Book updated: \n", jsonify(current_book)

@app.route('/bookshop/<int:id>', methods = ['DELETE'])
def remove_stock(id):
    found_books = list(filter(lambda t: t["id"] == id, bookshop))
    if len(found_books) == 0:
        return jsonify({}), 404
    bookshop.remove(found_books[0])
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug = True)