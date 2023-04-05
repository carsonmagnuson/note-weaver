from flask import Flask, jsonify
from collections import defaultdict
import uuid

app = Flask(__name__)
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

@app.route('/pieces', methods=['POST'])
def save_piece():
     new_piece = request.json
     new_id = str(uuid.uuid4())
     pieces[new_id] = new_piece

     return jsonify({'id': new_id}), 201


if __name__ == "__main__":
    app.run(debug=True)
