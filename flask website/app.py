from functools import wraps
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from werkzeug.local import F

from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

from input_processing import process_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ester_hydrolysis', methods = ['GET', 'POST'])
def ester_hydrolysis():
    # this renders the template home.html from the templates folder
    n = 1
    increment = 0
    values = []
    rows = []
    k = 0
    if request.method == 'POST':
        n = request.form['n']
        if n == '':
            n = 1
        else:
            n = int(n)
        increment = request.form['increment']
        # if these values are empty strings we can't run the float function on them
        if increment == '':
            increment = 0
        else:
            increment = float(increment)
        V_inf = request.form['V_inf']
        if V_inf == '':
            V_inf = 0
        else:
            V_inf = float(V_inf)

        # When we first select the number of rows, they don't exist yet, so we get a KeyError when we try to fetch them
        for i in range(1, n):
            try:
                values.append(request.form['Vt_' + str(i)])
            except KeyError:
                values.append(0)

        # Converting the list values from str to float
        values = list(map(float, values))
        app.logger.info(values)

        rows, k = process_input(values, increment, n, V_inf=V_inf)
        app.logger.info(rows)

    return render_template('ester_hydrolysis.html', n = n, values = values, rows = rows, k = k, increment = increment)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug= True)