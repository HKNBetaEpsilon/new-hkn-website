A HKN Website Using Django
==========

Set up on a Unix-like enviroment (Windows you're on your own)
==========

This website is built with the [Django Framework](https://www.djangoproject.com/). To get a
development environment set up, do the following:

1. Clone this repository

        $ git clone https://github.com/nimmerman/new-hkn-website.git

1. Setup virtualenv with Python:

        $ cd new-hkn-website
        $ virtualenv venv
        $ source venv/bin/activate

2. Install the dependencies:
        $ pip install django==1.9
        $ pip install python-social-auth
        $ pip install --upgrade django-crispy-forms
        $ pip install Pillow

3. Create the database

        $ cd src
        $ python manage.py makemigrations
        $ python manage.py migrate

4. Run the server as a Localhost

        $ python manage.py runserver

5. Open your web browser and go to http://127.0.0.1:8000/
