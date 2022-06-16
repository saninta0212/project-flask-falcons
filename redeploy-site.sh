#!/bin/bash

tmux kill-session -t $1
cd project-flask-falcons
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
cd app
tmux new -d -s $1 flask run --host=0.0.0.0
