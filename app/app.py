import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

import json

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="About Me", url=os.getenv("URL"))


@app.route('/experience')
def experience():
    data_path = os.path.join(app.static_folder, 'data', 'sambina_experience.json')
    job_list = json.load(open(data_path))

    return render_template('work_experience.html', title="Work Experience", url=os.getenv("URL"), job_list=job_list)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))


@app.route('/education')
def education():
    return render_template('education.html', title="Education", url=os.getenv("URL"))


@app.route('/places')
def places():
    countries = ["Canada", "Bangladesh", "India", "Thailand",
                 "Singapore", "Malaysia", "Hong Kong", "Dubai", "Saudi Arabia"]
    countries.sort()
    return render_template('places.html', title="Places Visited", url=os.getenv("URL"), countries=countries)


@app.route('/projects')
def projects():
    return render_template('projects_and_skills.html', title="Technical Skills & Projects", url=os.getenv("URL"))
