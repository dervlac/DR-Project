from flask import Flask, url_for, request, jsonify, abort, redirect
import requests
import json


app = Flask(__name__,static_url_path = '',static_folder = 'staticpages')

@app.route('/')
def index():
    return "Hello World!"

@app.route('/login')
def login():
    return "This page will be the login page"


if __name__ = "__main__":
    app.run(debug = True)