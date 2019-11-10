#!/usr/bin/env python
from flask import Flask,jsonify
import MongoClient

app = Flask(__name__)

@app.route('/cmdb/api/v1.0/hosts', methods=['GET'])
def get_tasks():
    pass
    #return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
