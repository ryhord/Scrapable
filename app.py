from flask import Flask, render_template
import scraping

app = Flask(__name__)

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)