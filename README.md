AirBnB Clone
Description

This project is the first step towards building an AirBnB clone. It focuses on creating a command interpreter that manages AirBnB objects.

The command interpreter allows users to create, retrieve, update, and destroy objects. It also implements serialization and deserialization using JSON file storage.

Command Interpreter

The console is a command-line interface that allows users to interact with AirBnB objects.

How to start it
bash
./console.py


Alternatively:

bash
python3 console.py

Available commands
Command	Description
quit	Exits the console
EOF	Exits the console
help	Displays available commands
create	Creates a new object
show	Displays an object
all	Displays all objects
destroy	Deletes an object
update	Updates an object's attributes
Project Structure
text
alche-Air_BnB/
├── AUTHORS
├── README.md
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
└── tests/
    ├── __init__.py
    └── test_models/
        └── __init__.py

Technologies
Python 3
JSON
CMD module
UUID
Datetime
Unittest
Authors
Leatitia Mizero
Kerubo Faith Ogoti
Usage

Run the console:

bash
./console.py


Example:

text
(hbnb) help
(hbnb) quit

Testing

Run the unit tests using:

bash
python3 -m unittest discover tests

License

This project was created for educational purposes.