from flask import Flask
from flask_cors import CORS
from router import user_router

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(user_router)

if __name__ == '__main__':
    app.run(debug=True)