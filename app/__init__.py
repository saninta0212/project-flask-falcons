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
    def format_job(title, date, organization, logo_url):
        return {
            "title": title,
            "date": date,
            "organization": organization,
            "logo_url": logo_url
        }

    job_list = [
        format_job("Undergrad Co-op - R&D (Data Informatics/Molecular Biology)", "May 2021 - December 2021", "Amgen",
                   "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.jobsexpo.ie%2Fwp-content%2Fuploads%2F2018%2F09%2FAmgen-Logo-PNG-Transparent-800.png&f=1&nofb=1"),
        format_job("Bioinformatics Technology Lab Co-op with Dr Inanc Birol", "September 2020 - April 2021", "BC Cancer Genome Sciences Centre",
                   "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2319317%3Fs%3D200%26v%3D4&f=1&nofb=1"),
        format_job("Undergraduate Research Assistant at Dr. Jamie Zeitzer’s lab", "May 2021- Present",
                   "Wu Tsai Neurosciences Institute at Stanford University", "https://neuroscience.stanford.edu/sites/g/files/sbiybj1576/f/neuro-signature-logo.png"),
        format_job("AMS Tutoring Supervisor", "September 2020 - Present",
                   "Alma Mater Society UBC", "https://duckduckgo.com/i/db0508c6.png"),
        format_job("AMS Tutor", "September 2019 - August 2020",
                   "Alma Mater Society UBC", "https://duckduckgo.com/i/db0508c6.png")
    ]
    return render_template('work_experience.html', title="Work experience", url=os.getenv("URL"), job_list=job_list)


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
    return render_template('places.html', title="Places", url=os.getenv("URL"), countries=countries)


@app.route('/projects')
def projects():
    return render_template('projects_and_skills.html', title="Projects & Skills", url=os.getenv("URL"))
