import os
import sys
from flask import Flask
from flask import request
from flask import render_template

sys.path.append(os.getcwd())
from agent import get_program

app = Flask(__name__)

@app.route("/")
def prompt():
    return render_template('index.html')

@app.route("/do_request", methods = ['POST'])
def do_request():
    prompt =  request.form.get('prompt')
    return render_template('program.html', program=get_program(prompt))