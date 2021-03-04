from flask import Flask
from api import test_api

app = Flask(__name__)

app.register_blueprint(test_api)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Team A^2</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
    app.run()
