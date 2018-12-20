import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def init():
    db.create_all()


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    guid = Column(String(36), unique=True, default=str(uuid.uuid1()))
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(32), nullable=False)
    authority = Column(Integer, default=0)

    def __repr__(self):
        return "<User(id='%s', guid='%s', username='%s',password='%s',authority='%s')>" \
               % (self.id, self.guid, self.username, self.password, self.authority)


class Function(db.Model):
    __tablename__ = 'function'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    guid = Column(String(36), unique=True, default=str(uuid.uuid1()))
    name = Column(String(255), unique=True, nullable=False)
    capacity = Column(Integer, default=1)


class StreamService(db.Model):
    __tablename__ = 'stream_service'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    guid = Column(String(36), unique=True, default=str(uuid.uuid1()))
    source_url = Column(String(255), nullable=False)
    function_id = Column(Integer, ForeignKey('function.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    result_rul = Column(String(255), default="")
