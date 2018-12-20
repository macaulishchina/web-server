from flask import Flask
from flask import jsonify

import dao
from dao import db,User,StreamService,Function

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/user/register', methods=['POST'])
def register():
    return "register"


@app.route('/initDB', methods=['GET'])
def initDB():
    dao.init()
    return "done"


@app.route('/addUser', methods=['GET'])
def addUser():
    root = User(username="root", password="root")
    db.session.add(root)
    db.session.commit()
    return "add"


@app.route('/query', methods=['GET'])
def queryAllUser():
    #print(dao.User.query.all())
    return "query"

