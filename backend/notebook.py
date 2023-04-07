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
    print(f'new id created at {new_id}')
    print(request.data)
    piece_type = request.json['type']
    world = request.json['world']
    content = request.json['content']
    characters = request.json['characters']
    date = str(datetime.datetime.now())
    new_piece = {
        'type': piece_type,
        'world': world,
        'content': content,
        'characters': characters,
        'date': date
        }
    pieces[new_id] = new_piece
    return {'message': 'Piece saved successfully'}

@app.route('/get', methods=['GET'])
def get():
    print('retrieving pieces...')
    return pieces

@app.route('/pieces/<piece_id>', methods=['PUT'])
def update_piece(piece_id):
    updated_data = request.json 
    pieces[piece_id].update(updated_data)
    
    return jsonify({"message": "piece updated"}), 200

if __name__ == "__main__":
    app.run()
