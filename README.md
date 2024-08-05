# ale_portfolio_devops

With this app you are able to CRUD users.

Table:
    Users
        id SERIAL
        first_name TEXT NON NULL,
        last_name TEXT NON NULL,
        email EMAIL NON NULL UNIQUE

endpoints:
    Users


To run the appliication:
make sure your docker desktop
docker compose up (-d)
docker compose exec web pyhton manage.py makemigrations (--noinput)
docker compose exec web python manage.py migrate (--noinput)


for django web page go to: http://127.0.0.1:8000

for pgAdmin go to: localhost: http://127.0.0.1:5433