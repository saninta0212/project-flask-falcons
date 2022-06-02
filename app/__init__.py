import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="About", url=os.getenv("URL"))


@app.route('/experience')
def experience():
    return render_template('work_experience.html', title="Work experience", url=os.getenv("URL"))
