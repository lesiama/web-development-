# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:28:25 2023

@author: olmal
"""

from flask import render_template, Flask, request

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/art_methods.html')
def art_methods():
    return render_template('art_methods.html')


@app.route('/science_methods.html')
def science_methods():
    return render_template('science_methods.html')     

@app.route('/digital_methods.html')
def digital_methods():
    return render_template('digital_methods.html')   


@app.route('/restoration_centers.html')
def restoration_centers():
    return render_template('restoration_centers.html')   

if __name__ == '__main__':
    app.run(debug=True)