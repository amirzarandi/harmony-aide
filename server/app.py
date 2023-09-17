from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/palliative"
db = SQLAlchemy(app)
CORS(app)

class Convo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text(), nullable = False)
    msg = db.Column(db.String(150), nullable = False)

    def __repr__(self):
        return f"Convo: {self.msg}"
    
    def __init__(self, username, msg):
        self.username = username
        self.msg = msg

def format_convo(convo):
    return {
        "id": convo.id,
        "username": convo.username,
        "msg": convo.msg
    }

@app.route('/')
def hello():
    return 'Hey!'

# create a conversation message
@app.route('/convos', methods = ['POST'])
def create_convo():
    username = request.json['username']
    msg = request.json['msg']
    convo = Convo(username, msg)
    db.session.add(convo)
    db.session.commit()
    return format_convo(convo)

# get all convos
@app.route('/convos', methods = ['GET'])
def get_convos():
    convos = Convo.query.order_by(Convo.id.asc()).all()
    convo_list = []
    for convo in convos:
        convo_list.append(format_convo(convo))
    return {'convos': convo_list}

# get single convo
@app.route('/convos/<id>', methods = ['GET'])
def get_convo(id):
    convo = Convo.query.filter_by(id=id).one()
    formatted_convo = format_convo(convo)
    return {'convo': formatted_convo}

# delete an event
@app.route('/convos/<id>', methods = ['DELETE'])
def delete_convo(id):
    convo = Convo.query.filter_by(id=id).one()
    db.session.delete(convo)
    db.session.commit()
    return f'Convo (id: {id}) deleted!'

if __name__ == '__main__':
    app.run()