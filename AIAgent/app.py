import os
import sys
from flask import Flask
from flask import request

sys.path.append(os.getcwd())
from agent import get_program

app = Flask(__name__)

@app.route("/")
def prompt():
    return ("<form action='/do_request' method='POST'>"
            "<input name='prompt' type='text' placeholder='Enter your request' />"
            "<input type='submit' />"
            "</form>")

@app.route("/do_request", methods = ['POST'])
def do_request():
    prompt =  request.form.get('prompt')
    return "<p>Your request [" + str(get_program(prompt)) + "]</p>"