from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi aplicación de Flask 😎'

@app.route('/html')
def html():
    return '<button>Dame click</button>'

@app.route('/user/<name>')
def hello(name):
    return f'Hola {name}'

@app.route('/login', methods=['POST']) # GET, POST, PUT, DELETE, PATCH
def login():
    if request.method == 'POST':
        return 'Login'
    
@app.route('/client', methods=['GET'])
def client():
    return {
        'id': 1,
        'name': 'Juan',
        'email': 'juan@gmail.com'
    }

if __name__ == '__main__':
    app.run(debug=True)