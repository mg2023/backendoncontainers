First you must create a docker image:
docker build -t app:v1 .

Second you must run docker compose in detached mode:
docker compose up -d

Thrid, connect to database adminer for create "users" table with just two colunmns: name and email boths of var char type.

And Finally, you need send a POST message to localhost:80/users with name and email fields for write on database and a GET message for read from date base.



