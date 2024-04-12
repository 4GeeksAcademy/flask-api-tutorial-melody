from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


# Supongamos que tienes tus datos en la variable some_data
todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)
    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text

#POST TODOS

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

# DELETE TODOS

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position <= len(todos):
        deleted_todo = todos.pop(position - 0)
        return jsonify(todos)

# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)