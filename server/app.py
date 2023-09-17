from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from chatbot import processText
from lipsync import lipSync
from TTS import tts

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
        if len(msg) > 150:
            self.msg = msg[-150:]
        else:
            self.msg = msg

def format_convo(convo):
    return {
        "id": convo.id,
        "username": convo.username,
        "msg": convo.msg
    }

def convo_toString(convo):
    return convo.username + ": " + convo.msg

# generate AI response
@app.route('/response', methods = ['POST'])
def get_response():
    input = request.json['input']
    convos = Convo.query.order_by(Convo.id.desc()).limit(4).all()
    convo_list = [convo_toString(convo) for convo in convos]
    memory = "\n".join(convo_list)
    return processText(input, memory)

# text to speech
@app.route('/tts', methods = ['POST'])
def get_tts():
    input = request.json['text'] 
    tts(input)
    return 'success'


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

@app.route('/lipsync', methods = ['POST'])
def lipsync():
    link = lipSync("https://storage.googleapis.com/palliative-ai/video.mp4", "https://github.com/amirzarandi/palliative-ai-2/blob/b1cd04f5262991ae59e2910a5c319938c8354c56/server/data/audio_ext.wav")
    return {'link': link}


if __name__ == '__main__':
    app.run()