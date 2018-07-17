from flask import Flask, render_template, request, redirect, url_for, jsonify

import scraping

app = Flask(__name__)

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    """redirect(url_for('results', url=request.form['url'], selection=request.form['selection']))"""
    """results(request.form['url'], request.form['selector'])"""


@app.route("/results", methods=['GET'])
def results():
    url = request.args['url']
    selector = request.args['selector']
    list_of_results = scraping.get_names(url, selector)
    for result in list_of_results:
        print(result)
    return render_template('results.html', list_of_results=list_of_results)


@app.route("/results/api", methods=['GET'])
def api():
    url = request.args['url']
    selector = request.args['selector']
    list_of_results = scraping.get_names(url, selector)
    return jsonify(list_of_results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    #app.run(debug=DEBUG, host=HOST, port=PORT)