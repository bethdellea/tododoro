from flask import Flask, render_template, request, url_for, flash, redirect
from config import *
from todo import *

app = Flask(__name__)
#key for flash messages
app.config['SECRET_KEY'] = SECRET_FLASH_KEY

success_message = False

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        print("POST SUBMITTED      ")
        form_data = dict(request.form)
        changes_stored = update_todo_items(form_data)
        if changes_stored:
            success_message = True
        else:
            success_message = False
    todo_return = get_todo_content()
    return render_template('index.html', openTasks=todo_return)

