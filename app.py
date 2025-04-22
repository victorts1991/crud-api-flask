from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if 0 <= item_id < len(items):
        items[item_id].update(data)
        return jsonify(items[item_id])
    return jsonify('error', 'item not found'), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        removed = items.pop(item_id)
        return jsonify(removed)
    return jsonify('error', 'item not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
