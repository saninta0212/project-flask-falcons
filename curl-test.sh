#!/usr/bin/env bash

curl --request GET http://localhost:5000/api/timeline_post
curl http://localhost:5000/api/timeline_post 


curl --request POST http://localhost:5000/api/timeline_post -d 'name=Sam&email=sambina@gmail.com&content=Checking endpoints'
  
curl -X  POST http://localhost:5000/api/timeline_post -d 'name=Sam&email=sambina@gmail.com&content=Checking endpoints'  

curl http://localhost:5000/api/timeline_post 
