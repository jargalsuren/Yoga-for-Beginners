# Yoga for Beginners
<img width="1680" alt="Screen Shot 2022-08-12 at 15 31 16" src="https://user-images.githubusercontent.com/65689294/184453625-9c3b7934-3ec3-430d-8436-f992e360fa25.png">
<img width="1680" alt="Screen Shot 2022-08-12 at 15 31 27" src="https://user-images.githubusercontent.com/65689294/184453643-f05e453c-64b1-42d1-9494-a6d9b534bb9c.png">
<img width="1680" alt="Screen Shot 2022-08-12 at 15 31 32" src="https://user-images.githubusercontent.com/65689294/184453653-9547bedc-70ac-4208-bb38-44fe95923203.png">
<img width="1680" alt="Screen Shot 2022-08-12 at 15 31 38" src="https://user-images.githubusercontent.com/65689294/184453657-910ab1b6-729e-46c1-91a3-6a9d984d8cd2.png">

## Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:

    $ virtualenv -p python3 venv

If the above code does not work, you could also do

    $ python3 -m venv venv

To activate the virtualenv:

    $ source venv/bin/activate

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate

Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt

## Environment Variables

All environment variables are stored within the `.env` file and loaded with dotenv package.

**Never** commit your local settings to the Github repository!

## Run Application

Start the server by running:

    $ export FLASK_ENV=development
    $ export FLASK_APP=web
    $ python3 -m flask run

Note: when installing flask using the command above one might run into an issue of missing a required module(s). In order to solve it you might need to install the following modules if an error occurs:

    $ pip install flask
    $ pip install 'flask_sqlalchemy'
    $ pip install flask_login
    $ pip install 'flask_bcrypt'
    $ pip install 'flask_wtf'
    $ pip install email_validator
    
## Unit Tests
To run the unit tests use the following commands:

    $ python3 -m venv venv_unit
    $ source venv_unit/bin/activate
    $ pip install -r requirements-unit.txt
    $ export DATABASE_URL='sqlite:///web.db'
    $ pytest unit_test

## Integration Tests
Start by running the web server in a separate terminal.

Now run the integration tests using the following commands:

    $ python3 -m venv venv_integration
    $ source venv_integration/bin/activate
    $ pip3 install -r requirements-integration.txt
    $ pytest integration_test

## Deployment
We will use Heroku as a tool to deploy your project, and it is FREE

We added Procfile to help you deploy your repo easier, 
but you may need to follow these steps to successfully deploy the project

1. You need to have admin permission to be able to add and deploy your repo to Heroku 
(Please ask your professor for permission)
2. You need to create a database for your website. 
We recommend you use [Heroku Postgres](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1)
3. You may need to add environment variables to deploy successfully - [Resource](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard)
