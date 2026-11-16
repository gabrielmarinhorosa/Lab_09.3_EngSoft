from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
next_id = 3


def find_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)


def read_name():
    """Return the "name" sent in the JSON body, or None if it is missing or invalid."""
    body = request.get_json(silent=True)
    name = body.get("name") if isinstance(body, dict) else None
    if isinstance(name, str) and name.strip():
        return name.strip()
    return None


# Home page (kept from exercise 9.3)
@app.route("/")
def hello_world():
    return "Hello, World!"


# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items})


# Get a specific item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify({"item": item})
    return jsonify({"error": "Item not found"}), 404


# Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    global next_id
    name = read_name()
    if name is None:
        return jsonify({"error": "Field 'name' is required"}), 400
    new_item = {"id": next_id, "name": name}
    next_id += 1
    items.append(new_item)
    return jsonify({"item": new_item}), 201


# Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    name = read_name()
    if name is None:
        return jsonify({"error": "Field 'name' is required"}), 400
    item["name"] = name
    return jsonify({"item": item})


# Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    items.remove(item)
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)
