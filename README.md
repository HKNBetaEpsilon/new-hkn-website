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

        $ pip install -r requirements.txt

3. Create the database

        $ cd src
        $ python manage.py migrate

4. Run the server as a Localhost

        $ python manage.py runserver

5. Open your web browser and go to http://127.0.0.1:8000/

6. To set up log in with your uniqname, do the following:
  1. Run this command and follow the promts (**do not** use your uniqname as the username)
    
        $ python manage.py createsuperuser

  2. Navigate to http://127.0.0.1:8000/admin and login in as the user you just created
  3. At the bottom of the page, click on "Members" under the "Users" Section
  4. In the top right corner, click on "Add Member"
  5. Type in your uniqname and click "save"
  6. In navigation bar at the top right corner, click "logout" and the "view site"
  7. Click "login" and login in with your uniqname

7. If you would like to give your uniqname account superuser status (be able to view the tools tab and electee managment tab)
  1. Go to http://127.0.0.1:8000/admin and login in as with the superuser you created in step 6
  2. Under the AUTHENTICATION AND AUTHORIZATION section click on Users
  3. Click on your uniqname
  4. Under Permissions, check the boxes "Staff status" and "Superuser status" and click "Save"
  5. Click "Log out" and "View site" and then login with your uniqname 