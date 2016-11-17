# Apptimize Decision Time: Flask

This includes simple examples of a database driven web app 
written in Flask + SQLAlchemy.  Also included are examples 
on authentication, configuration (and incidentally dependency 
injection), and middleware in Python.  All of these are largely
framework independent and would work in almost any python 
web framework.

As a bonus, I also included an example of the same application
using `ripozo` which sits on top of Flask and helps you create 
a truly RESTful application with a variety of HATEOAS specs.  Just
by changing you `Content-Type` header, you can choose how you want
the resources represented.  

## The Application

This application is a simple User and Group web app.  Users and Groups
are a many to many relationship.  The application allows you to create
users, groups, and manage the relationships between them.  It is
imperative that it uses appropriate status codes and verbs.  


## Structure

There are four major sections for this repo. 
* `myapp`: simple Flask app with few dependencies
* `myapp_tests`: Example unit and functional tests
* `bonus`: Additional patterns for configuration, dependency injection, middleware, and authentication
* `myapp_ripozo`: The same application as `myapp` implemented using `ripozo`

## Installation

1. Install [Docker for Mac](https://docs.docker.com/docker-for-mac/)
2. cd to the root of this directory
3. Run `docker-compose build`
4. Run `docker-compose up`

That's it.  You can now access the basic app on `localhost:5000` and
the ripozo version on `localhost:4000`

If you just want to run the simple version do: `docker-compose up myapp`. 
Alterntivately for the `ripozo` version: `docker-compose up myapp-ripozo`.

## Testing

After installing the application simply run
```
docker-compose run myapp test
```

## Play with the walk-through

For the ripozo app, there is a simple walkthrough that you can do by running
`bin/ripozo.sh` on your local machine.  It will curl against the application
and offer really dumb insights into what is happening.  Simply press any key
to continue.

NOTE: The ripozo application must be running.  Starting up the docker container
from the `Installation` instructions is the easiest way.

## Helpful Links

* [Flask](http://flask.pocoo.org/)
    * [Flask Quickstart](http://flask.pocoo.org/docs/0.11/quickstart/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
    * [SQLAlchemy ORM](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html)  (Note: Flask-SQLAlchemy makes it very easy to manage the sessions and such)
    * [SQLAlchemy ORM Tutorial Again](http://pythoncentral.io/sqlalchemy-orm-examples/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
    * [Flask-SQLAlchemy Quickstart](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/)
* [ripozo](http://ripozo.org/en/latest/)
    * [flask-ripozo](https://flask-ripozo.readthedocs.io/en/latest/)
    * [ripozo-sqlalchemy](http://ripozo-sqlalchemy.readthedocs.io/en/latest/)
