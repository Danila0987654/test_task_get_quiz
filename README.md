# Test Task Get a Quiz
This project for a test task


## Table of Contents
- [Environment Variables](#environment-variables)
- [Run Locally](#run-locally)


## Environment Variables
To run this project, you will need to add the 
following environment variables 
to your .env file

***
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    POSTGRES_PORT=
    FLASK_HOST=
    FLASK_PORT=
    FLASK_DEBUG=
    FLASK_SECRET_KEY=
    SQLALCHEMY_TRACK_MODIFICATIONS=
***


## Run Locally
Clone the project

```bash
git clone https://github.com/Danila0987654/test_task_get_quiz.git
```

Go to the project directory

```bash
cd test_task_get_quiz
```

Launch docker-compose

```bash
docker-compose up -d
```

Init and migrate db:

```bash
flask db init
flask db migrate
flask db upgrade
```