#!/bin/bash

tmux kill-session -t $1
cd project-flask-falcons
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux -d new -s $1
cd app
export FLASK_ENV=development
flask run


