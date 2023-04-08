from flask import Flask, request
#from collections import defaultdict
from flask_cors import CORS
import uuid, datetime

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

ex_maple_id = str(uuid.uuid4())

pieces = {ex_maple_id:{
    'type': 'quote',
    'content': 'The man sat like a boulder in the rain, coiled beneath the gray sky.',
    'world': 'msc',
    'characters': 'NA', 
    'date': 'today'}
          }

@app.route('/create', methods=['POST'])
def create():        
    new_id = str(uuid.uuid4())
    date = str(datetime.datetime.now())

    print(f'new id {new_id} created at {date}')

    new_piece = {
        'date': date,
        'type': request.json['type'],
        'world': request.json['world'],
        'content': request.json['content'],
        'characters': request.json['characters'],
        }

    pieces[new_id] = new_piece
    return {'message': 'piece saved successfully'}

@app.route('/get', methods=['GET'])
def get_pieces():
    print('retrieving pieces...')
    return pieces

@app.route('/pieces/<piece_id>', methods=['GET', 'PUT'])
def modify_piece(piece_id):
    if request.method == 'GET':
        return pieces[piece_id]
    elif request.method == 'PUT':
        updated_piece = {
            'date': pieces[piece_id]['date'],
            'type': request.json['type'],
            'world': request.json['world'],
            'content': request.json['content'],
            'characters': request.json['characters'],
                }
        pieces[piece_id] = updated_piece
        return {'message': 'piece updated'}, 200
    else:
        return {"message": "error updating, wrong method"}, 404

if __name__ == "__main__":
    app.run()
