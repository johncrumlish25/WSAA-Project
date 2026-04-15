# WSAA Project – Football Players API
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

- app.py  
- database.db (ignored in Git)  
- README.md  
- templates/
  - index.html  

## How to Run the Project
##### 1. Clone the repository
git clone https://github.com/johncrumlish25/WSAA-Project.git

##### 2. Navigate into the project folder
cd WSAA-Project

##### 3. Install Flask
pip install flask

##### 4. Run the application
python app.py

##### 5. Open in browser
http://127.0.0.1:5000/

## Notes
- Data is stored in a SQLite database (`database.db`)
- The database file is excluded from version control using `.gitignore`
- The application runs locally and does not require external hosting
