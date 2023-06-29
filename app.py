from flask import Flask, jsonify

app = Flask(__name__)

app.config['MY_SPECIAL_CONFIGURATION_VAR'] = 'hello world'

print(app.config['MY_SPECIAL_CONFIGURATION_VAR'])

@app.route('/')
def home():
    """homepage"""
    return "Welcome to to-do API Service"

@app.route('/todos', methods=['GET'])
def get_tasks():
    """api route to retrieve all tasks"""
    return jsonify({ 'tasks': [{'name': 'get milk'}, {'name': 'get bread'}]})

@app.route('/todos', methods=['POST'])
def add_task():
    """api route to add a new task"""
    return jsonify({'imaginary new task': 'does not exist'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
