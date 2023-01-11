from os import stat
from flask import *
from os.path import exists
import pandas as pd
import json
from RepositoryDB import RepositoryDB

app = Flask(__name__)
rep = RepositoryDB()

@app.route('/')
def index():
    return render_template("index.html", data = getData())

@app.route('/login', methods=['POST'])
def login():
    data = str(request.data)
    data = data[3:-2]
   
    rep.connect()
    validate = rep.login(data)
    rep.disconnect()

    if validate:
        return jsonify({'return': True})
    else:
        return jsonify({'return': False})

@app.route('/updatePassword', methods=['POST'])
def updatePwd():
    data = str(request.data)
    data = data[3:-2]
   
    rep.connect()
    validate = rep.updatePWD(data)
    rep.disconnect()

    if validate:
        return jsonify({'return': True})
    else:
        return jsonify({'return': False})

@app.route('/getStatistics', methods=['GET'])
def getStat():
    data = getData()
    return json.dumps(data[2])

@app.route('/uploadData', methods=['POST'])
def uploadData():
    d = str(request.data)
    d = d[2:-1]
    d = json.loads(d)
    
    rep.connect()
    rep.deleteStatistics()
    rep.insertStatistics(d)
    rep.disconnect()  
    return jsonify({"return": True})

def getData():
    rep.connect()
    statistics = rep.getStatistics()
    rep.disconnect()

    dataP = {'Symbole' : 'in Prozent', 'Schere' : statistics['PLAYER'][2], 'Stein' : statistics['PLAYER'][3], 'Papier' : statistics['PLAYER'][4],
     'Spock' : statistics['PLAYER'][5], 'Echse' : statistics['PLAYER'][6]}

    dataC = {'Symbole' : 'in Prozent', 'Schere' : statistics['COMP'][2], 'Stein' : statistics['COMP'][3], 'Papier' : statistics['COMP'][4],
     'Spock' : statistics['COMP'][5], 'Echse' : statistics['COMP'][6]}

    data = [dataP, dataC, statistics, True]

    return data

if __name__ == '__main__':
    app.run(debug=True,threaded=True)