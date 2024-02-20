# 0x0F. Python - Object-relational mapping

## Description
This project is part of the ALX Africa curriculum. It covers the basics of object-relational mapping (ORM) in Python, using the MySQLdb and SQLAlchemy modules to interact with a MySQL database.

## Learning Objectives
- Understand the awesomeness of Python programming.
- Connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations in MySQL from Python.
- Grasp the concept of Object-Relational Mapping (ORM).
- Map a Python class to a MySQL table.

## Requirements
- Python 3.4.3 or higher
- MySQL 5.7 or higher
- MySQLdb module version 1.3.x
- SQLAlchemy module version 1.2.x
- PEP8 style

## Files
The following files are included in this project:

| File | Description |
| ---- | ----------- |
| 0-select_states.py | A script that lists all states from the database hbtn_0e_0_usa |
| 1-filter_states.py | A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa |
| 2-my_filter_states.py | A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument |
| 3-my_safe_filter_states.py | A script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa, avoiding SQL injection |
| 4-cities_by_state.py | A script that lists all cities from the database hbtn_0e_4_usa |
| 5-filter_cities.py | A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa |
| 6-model_state.py | A Python file that contains the class definition of a State and an instance Base = declarative_base() |
| 7-model_state_fetch_all.py | A script that lists all State objects from the database hbtn_0e_6_usa |
| 8-model_state_fetch_first.py | A script that prints the first State object from the database hbtn_0e_6_usa |
| 9-model_state_filter_a.py | A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa |
| 10-model_state_my_get.py | A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa |
| 11-model_state_insert.py | A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa |
| 12-model_state_update_id_2.py | A script that changes the name of a State object from the database hbtn_0e_6_usa |
| 13-model_state_delete_a.py | A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa |
| 14-model_city_fetch_by_state.py | A Python file that contains the class definition of a City |
| model_city.py | A script that prints all City objects from the database hbtn_0e_14_usa |
| 100-relationship_states_cities.py | A Python file that contains the class definition of a State and a City, linked by a relationship |
| 101-relationship_states_cities_list.py | A script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa |
| 102-relationship_cities_states_list.py | A script that lists all City objects from the database hbtn_0e_101_usa |

## Usage
To use these scripts, you need to have a MySQL server running on localhost at port 3306, and a database named hbtn_0e_0_usa, hbtn_0e_4_usa, hbtn_0e_6_usa, hbtn_0e_14_usa, or hbtn_0e_101_usa, depending on the script. You also need to have the MySQLdb and SQLAlchemy modules installed for Python.

To run the scripts, use the following command:

```bash
./<script_name> <mysql_username> <mysql_password> <database_name> [<state_name>]

