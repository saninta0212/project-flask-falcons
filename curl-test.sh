#!/usr/bin/env bash

  
curl -X  POST http://localhost:5000/api/timeline_post -d 'name=Sam&email=sambina@gmail.com&content=Checking endpoints'  

curl http://localhost:5000/api/timeline_post 

curl -X DELETE http://localhost:5000/api/timeline_post -d "id=$POST_ID"

