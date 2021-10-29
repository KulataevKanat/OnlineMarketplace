# Online Marketplace API

## Table of Contents

* Setup Instructions
* Documentation

## Setup instructions

1. Make sure you have python installed
2. Clone the repository
3. In the folder where the repository was cloned create a virtual environment using virtualenv venv
4. Activate the virtual environment by running (on Windows)

``````
venv\Scripts\activate
``````

6. Install the dependencies using (the package manager [pip](https://pip.pypa.io/en/stable/))

``````
pip install -r requirements.txt 
``````

7. Migrate existing database tables by running

``````
python manage.py migrate
``````

9. Run the server using

``````
python manage.py runserver
``````

## Documentation

* Link to the API [Swagger Documentation](http://127.0.0.1:8000/swagger/)
* Link to the API [Redoc Documentation](http://127.0.0.1:8000/redoc/)