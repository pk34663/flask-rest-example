import json
from flask import Flask,jsonify
import app.dbservice.mongoservice as MongoService

app = Flask(__name__)

mongoinstance = MongoService.MongoService('testdb')

@app.route('/cmdb/api/v1.0/hosts', methods=['GET'])
def get_tasks():
    hosts = mongoinstance.findAllCollection('hosts')
    return jsonify({'results':hosts})

if __name__ == '__main__':
    app.run(debug=True)
