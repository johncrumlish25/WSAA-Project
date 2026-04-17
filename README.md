# WSAA Project – Football Players API

## Overview
This project is a Flask web application that demonstrates the creation and use of a RESTful API.
The application allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of football players and their goal statistics.

## Features Implemented
- REST API built using Flask
- JSON data handling using Flask
- CRUD functionality:
  - GET – retrieve all players
  - POST – add a new player
  - PUT – update an existing player
  - DELETE – remove a player

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- JavaScript (Fetch API)
- Bootstrap

## Project Structure
- **app.py** – Flask application and API routes  
- **playerDAO.py** – Handles all database operations  
- **schema.sql** – Defines the database structure  
- **createschema.py** – Script to initialise the database  
- **dbconfig.py** – Stores database configuration  
- **templates/**
  - index.html – Frontend interface  
- **database.db** – SQLite database (ignored in Git)  
- **README.md**

## How to Run the Project
##### 1. Clone the repository
git clone https://github.com/johncrumlish25/WSAA-Project.git

##### 2. Navigate into the project folder
cd WSAA-Project

##### 3. Install Flask
pip install flask

##### 4. Initialise the database
python createschema.py

##### 5. Run the application
python app.py

##### 6. Open in browser
http://127.0.0.1:5000/

## Notes
- The database schema is defined in `schema.sql` and created using `createschema.py`
- SQLite is used for data storage
- The database file (`database.db`) is excluded from version control using `.gitignore`
- The application can be run locally or deployed on PythonAnywhere