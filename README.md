# PROJECT-3-CLI# phase-3-project-cli

# Movies Reviews application

# Description

This project is a movie reviews management system. It allows users to manage movies, user accounts and reviews using sqlite as the database backend. It is designed to perform basic CRUD such as create,read,update and delete operations from the python classes. Has the database/connection.py to handle the database connection and provide cursor for executing sql commands.
The models/movies.py contains the movies class for managing movie records. The models/users.py contains the users class for managing the users accounts. The models/reviews.py contains the reviews class for managing movie reviews.
All the classes are responsible for managing records. They support basic CRUD functions and they all manage a dictonary (all) to store objects by their IDS.

## Introduction

You now have a basic idea of what constitutes a CLI. Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── cli.py
├── __init__.py
├── license
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── movies.py
    │   ├── users.py
    │   └── reviews.py
```

## How to Use

### Requirements

1. Clone this repository using

```bash
 https://github.com/luvley-dee48/phase-3-project-cli

```

2. Navigate to the project folder on your bash terminal.

3. Install dependancies using

```bash
   pipenv install
```

4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
5. Run the application using the **init**.py and the cli.py

## Technologies Used

- Python
- SQLite
- Pipenv

## Features

- Add, update, and delete movie records
- Add, update, and delete user records
- Add, update, and delete reviews
- CLI

## Support and Contact Details

