# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:47:52 2019

@author: bailey wilder

"""
import os
import json
from flask import Flask, request,jsonify, redirect, render_template, session, url_for,g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')

@app.route('/',methods=['GET','POST'])

def calculate():
    x = 1
    y = 1
    z = []
    primeList = []
    errorMsg = "Enter positive whole numbers.  In the url (Example) ?json=1&Low=1&High=15"

    t = {'Low': 0, 'High': 0, 'Primes': 0}
    if request.method == 'POST':
       t['Low'] = request.form['Low']
       t['High'] = request.form['High']
    elif 'Low' in request.args:
       t['Low'] = request.args.get('Low')
       t['High'] = request.args.get('High')
       x = int(t['Low'])
       y = int(t['High'])

       z = range(int(x),int(y)+1)
    if x > 0 and y > 0:
       for numb1 in z:
           if numb1 > 1:
               for i in range(2,numb1):
                   if(numb1 % i) == 0:
                       break
               else:
                 primeList.append(numb1)
       t['Primes'] = primeList
       if 'json' in request.args:
           return jsonify(t['Primes'])
    else:
        t['Primes'] = errorMsg
        return jsonify(t['Primes'])

    if 'times' not in session:
        session['times'] = 0
    session['times'] += 1

    return render_template('index.html', t = t, times = session['times'])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('calculate'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
