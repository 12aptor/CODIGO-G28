from flask import Flask
from router import user_router

app = Flask(__name__)

app.register_blueprint(user_router)

if __name__ == '__main__':
    app.run(debug=True)