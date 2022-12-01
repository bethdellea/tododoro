from flask import Flask, render_template, request, url_for, flash, redirect
from config import *
from todo import *

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    todoReturn = get_todo_content()
    return render_template('index.html', openTasks=todoReturn)


#escape() please and thank you
