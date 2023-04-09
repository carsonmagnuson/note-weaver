from collections import defaultdict
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import uuid, datetime, os

app = Flask(__name__)
CORS(app)

load_dotenv()
API_KEY = os.getenv('API_KEY')
cluster = MongoClient(API_KEY) 
print(f'cluster = {cluster}')
pieces = cluster['noteweaves']['pieces']

ex_maple_id = str(uuid.uuid4())
test_pieces = {ex_maple_id:{
    'type': 'quote',
    'content': 'The man sat like a boulder in the rain, coiled beneath the gray sky.',
    'world': 'msc',
    'characters': 'NA', 
    'date': 'today'}
          }

#insert test Data
#pieces.insert_one(test_pieces)

@app.route('/create', methods=['POST'])
def create():        
    new_id = str(uuid.uuid4())
    date = str(datetime.datetime.now())

    print(f'new id {new_id} created at {date}')
    new_piece = { new_id: {
        'date': date,
        'type': request.json['type'],
        'world': request.json['world'],
        'content': request.json['content'],
        'characters': request.json['characters']
        }}

    pieces.insert_one(new_piece)
    return {'message': 'piece saved successfully'}

@app.route('/get', methods=['GET'])
def get_pieces():
    print('retrieving pieces...')
    retrieved = defaultdict()
    found = list(pieces.find())
    for piece in found:
        keys = list(piece.keys())
        key = max(keys, key=lambda x: len(x))
        retrieved[key] = piece[key]
    return retrieved

@app.route('/pieces/<piece_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_piece(piece_id):
    if request.method == 'GET':
        returnable = pieces.find_one({piece_id: {'$exists': True}})
        return returnable[piece_id]    
    elif request.method == 'PUT':
        update = {'$set': {
            f'{piece_id}.date': pieces.find_one({piece_id: {'$exists': True}})[piece_id]['date'],
            f'{piece_id}.type': request.json['type'],
            f'{piece_id}.world': request.json['world'],
            f'{piece_id}.content': request.json['content'],
            f'{piece_id}.characters': request.json['characters']
                }}
        pieces.update_one({piece_id: {'$exists': True}}, update)
        return {'message': 'piece updated'}, 200
    elif request.method == 'DELETE':
        pieces.delete_one({piece_id: {'$exists': True}})
        return {'message': 'piece deleted'}, 200
    else:
        return {"message": "error updating, wrong method"}, 404

if __name__ == "__main__":
    app.run()
