from flask import Flask, render_template, request, redirect, url_for
import scraping

app = Flask(__name__)

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print(request.form)
        print(request.form['url'])
        print(request.form['selector'])
        url = request.form['url']
        selection = request.form['selector']
        return redirect(url_for('results', url=url, selection=selection ))

    """redirect(url_for('results', url=request.form['url'], selection=request.form['selection']))"""
    """results(request.form['url'], request.form['selector'])"""

@app.route("/results", methods=['GET'])
def results():
    url = request.args['url']
    selection = request.args['selection']
    list_of_results = scraping.get_names(url, selection)
    for result in list_of_results:
        print(result)
    return render_template('results.html', list_of_results=list_of_results)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)