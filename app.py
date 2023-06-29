from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)


# TODO: MYSQL CONFIG VALUES NOT CORRECT FOR WORKING WITH DEFAULT MYSQL DOCKER IMAGE
# APP TALKS TO MYSQL SERVER BUT CONNECTION REFUSED
# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'todo'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'

mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

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
