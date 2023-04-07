from flask import Flask, jsonify
#from collections import defaultdict
from flask_cors import CORS
import uuid

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

@app.route('/pieces', methods=['GET'])
def get_pieces():

    return jsonify(pieces)

@app.route('/', methods=['POST'])
def create_piece():
    print('new piece detected')
    new_piece = request.get_json()
    new_id = str(uuid.uuid4())
    pieces[new_id] = new_piece
    print(pieces)

    return jsonify({'id': new_id}), 201

@app.route('/pieces/<piece_id>', methods=['PUT'])
def update_piece(piece_id):
    updated_data = request.json 
    pieces[piece_id].update(updated_data)
    
    return jsonify({"message": "piece updated"}), 200

if __name__ == "__main__":
    app.run(debug=True)
