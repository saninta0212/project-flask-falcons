import os
import re
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json
from playhouse.shortcuts import model_to_dict
from werkzeug import exceptions

from app.mydb import TimelinePost

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


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    email_regex = re.compile(r"([A-Za-z0-9]+[--.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

    key = ""
    try:
        key = "name"
        name = request.form[key]
        if len(name) == 0:
            raise exceptions.BadRequestKeyError(key)

        key = "email"
        email = request.form[key]
        is_email_valid = re.fullmatch(email_regex, email)
        if len(email) == 0 or not is_email_valid:
            raise exceptions.BadRequestKeyError(key)

        key = "content"
        content = request.form[key]
        if len(content) == 0:
            raise exceptions.BadRequestKeyError(key)

    except exceptions.BadRequestKeyError:
        """
        BadRequestKeyError is raised by default when the body doesn't contain any of name, email or content.
        Additionally, these statements:
            if len(name) == 0: ...
            if len(email) == 0 or not is_email_valid: ...
            if len(content) == 0: ...
        also raise BadRequestKeyError if some other conditions aren't fulfilled
        """
        return f"Invalid {key}", 400

    time_line_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(time_line_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {'timeline_post': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}


@app.route('/api/timeline_post', methods=['DELETE'])
def delete_post():
    post_id = request.form['id']
    TimelinePost.delete_by_id(post_id)
    return "Delete Successful"


@app.route('/timeline')
def timeline():
    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template('timeline.html', title="Timeline of Activities and Experience", content=timeline_posts)
