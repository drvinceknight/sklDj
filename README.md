# sklDj

[![Join the chat at https://gitter.im/drvinceknight/sklDj](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/drvinceknight/sklDj?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/drvinceknight/sklDj.svg?branch=master)](https://travis-ci.org/drvinceknight/sklDj)

A django site as an interface to [sci-kit learn](http://scikit-learn.org/stable/).

# Setup

Setup a virtual env:

    cd sklDj
    virtualenv env

Activate virtual env:

    source env/bin/activate

Install requirements:

    pip install -r requirements.txt

(If you have any errors update pip: `pip install --upgrade pip`)

Navigate to the directory containing manage.py:

    cd sklDj/

Ensure database up to date:

    python manage.py migrate

Run the server:

    python manage.py runserver

Create a super user:

    python manage.py createsuperuser
