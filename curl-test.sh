#!/usr/bin/env bash
 

# deletes 60 posts 
for i in {1..65}; do curl -X DELETE http://localhost:5000/api/timeline_post -d "id=$i"; done;

curl -X  POST http://localhost:5000/api/timeline_post -d 'name=Sam&email=sambina@gmail.com&content=Checking endpoints'

curl http://localhost:5000/api/timeline_post
