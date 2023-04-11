from collections import defaultdict
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
import uuid, datetime, os

from pymongo.mongo_client import _retryable_error_doc

app = Flask(__name__)
CORS(app)

load_dotenv()
MONGO_KEY= os.getenv('MONGO_KEY')
cluster = MongoClient(MONGO_KEY) 
print(f'cluster = {cluster}')
pieces = cluster['noteweaves']['pieces']

test_pieces = {
    'type': 'quote',
    'content': 'The man sat like a boulder in the rain, coiled beneath the gray sky.',
    'world': 'msc',
    'characters': 'NA', 
    }

#insert test Data
pieces.insert_one(test_pieces)
print(next(pieces.find())['_id'])

@app.route('/create', methods=['POST'])
def create():        
    print(f'new piece created at {date}')
    new_piece = {
        'type': request.json['type'],
        'world': request.json['world'],
        'content': request.json['content'],
        'characters': request.json['characters']
        }

    pieces.insert_one(new_piece)
    return {'message': 'piece saved successfully'}

@app.route('/get', methods=['GET'])
def get_pieces():
    print('retrieving pieces...')
    found = list(pieces.find({}))
    for piece in found:
        piece['_id'] = str(piece['_id'])
    # found = json_util.dumps(found) 

    return found

@app.route('/pieces/<piece_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_piece(piece_id):
    print(f'{piece_id} is piece id')
    if request.method == 'GET':
        returnable = pieces.find_one({'_id': ObjectId(piece_id)})
        returnable['_id'] = str(returnable['_id'])
        return json_util.dumps(returnable) 

    elif request.method == 'PUT':
        update = {'$set': {
            f'type': request.json['type'],
            f'world': request.json['world'],
            f'content': request.json['content'],
            f'characters': request.json['characters']
                }}
        pieces.update_one({'_id': ObjectId(piece_id)}, update)
        return {'message': 'piece updated'}, 200
    elif request.method == 'DELETE':
        pieces.delete_one({'_id': ObjectId(piece_id)})
        return {'message': 'piece deleted'}, 200
    else:
        return {"message": "error updating, wrong method"}, 404

if __name__ == "__main__":
    app.run()
