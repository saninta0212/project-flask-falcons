import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()

def create_app():

    app=Flask(__name__)


    @app.route('/')
    def index():

        return render_template('index.html', title="About Me", url=os.getenv("URL"))


    @app.route('/experience')
    def experience():
        return render_template('work_experience.html', title="Work Experience", url=os.getenv("URL"))


    @app.route('/hobbies')
    def hobbies():
        return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))


    @app.route('/education')
    def education():
        return render_template('education.html', title="Education", url=os.getenv("URL"))


    @app.route('/places')
    def places():
        return render_template('places.html', title="Places visited", url=os.getenv("URL"))


    @app.route('/projects')
    def projects():
        return render_template('projects_and_skills.html', title="Technical Skills and Projects", url=os.getenv("URL"))

    return app

app = create_app()
