from os import stat
from flask import *
from os.path import exists
import pandas as pd
import json
#from SchereStein.RepositoryDB import RepositoryDB

app = Flask(__name__)
#rep = RepositoryDB()

@app.route('/')
def index():
    return render_template("index.html", data = getData())

@app.route('/getStatistics', methods=['GET'])
def getStat():
    data = getData()
    return json.dumps(data[2])

@app.route('/uploadData', methods=['POST'])
def uploadData():
    d = str(request.data)
    d = d[2:-1]
    d = json.loads(d)
    print(d['PLAYER'][0])
    #   rep.connect()
    #   rep.deleteStatistics()
    #   rep.insertStatistics(statistics)
    #   rep.disconnect()  
    return jsonify({"return": True})

def getData():
    # rep.connect()
    # statistics = rep.getStatistics()
    # rep.disconnect()
    statistics = {"PLAYER" : [1, 1, 5, 8, 5, 10, 2], "COMP" : [2, 1, 3, 3, 3, 3, 3]}

    dataP = {'Symbole' : 'in Prozent', 'Schere' : statistics['PLAYER'][2], 'Stein' : statistics['PLAYER'][3], 'Papier' : statistics['PLAYER'][4],
     'Spock' : statistics['PLAYER'][5], 'Echse' : statistics['PLAYER'][6]}

    dataC = {'Symbole' : 'in Prozent', 'Schere' : statistics['COMP'][2], 'Stein' : statistics['COMP'][3], 'Papier' : statistics['COMP'][4],
     'Spock' : statistics['COMP'][5], 'Echse' : statistics['COMP'][6]}

    data = [dataP, dataC, statistics, True]

    return data

if __name__ == '__main__':
    app.run(debug=True,threaded=True)