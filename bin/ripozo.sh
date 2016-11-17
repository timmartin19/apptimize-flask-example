#!/bin/bash -ex

curl http://localhost:4000/api/user/ | jq .

read -n 1 -p "Create a new user!: "
curl -X POST http://localhost:4000/api/user/ -d '{"username": "bob123", "first_name": "Bob"}' | jq .

read -n 1 -p "Attempt to create an invalid user :( "
curl -X POST http://localhost:4000/api/user/ -d '{"username": "b", "first_name": "Bob"}' | jq .

read -n 1 -p "Create another user and then fetch all users : "
curl -X POST http://localhost:4000/api/user/ -d '{"username": "alice", "first_name": "Alice"}' | jq .
curl http://localhost:4000/api/user/ | jq .

read -n 1 -p "Follow the user links...: "
user_ref=`curl http://localhost:4000/api/user/ | jq '._links.user[0].href' | sed -e 's/"//g'`
curl "http://localhost:4000/api${user_ref}" | jq .
user_id=`curl http://localhost:4000/api${user_ref} | jq .id | sed -e 's/"//g'`

read -n 1 -p "Create a group and add a user to it: "
group_id=`curl -X POST http://localhost:4000/api/group/ -d '{"name": "bobsgroup"}' | jq .id | sed -e 's/"//g'`
curl -X POST http://localhost:4000/api/user_group/ -d "{\"user_id\": \"${user_id}\", \"group_id\": ${group_id}}" | jq .

read -n 1 -p "Get the group back with the embedded users! "
curl http://localhost:4000/api/group/${group_id}/ | jq .
