'''
Team PaPaPandas - Johnny Wong and Jack Lu
SoftDev2 pd8
P#03 -- You Are the Expert: TEDxSoftDev 2019
2019-04-30
'''

import os

from flask import Flask, render_template, redirect, url_for, session, request

#==========instantiate Flask object=====================
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
