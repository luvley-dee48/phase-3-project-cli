# PROJECT-3-CLI# phase-3-project-cli

# Movies Reviews application

# Description

This project is a movie reviews management system. It allows users to manage movies, user accounts and reviews using sqlite as the database backend. It is designed to perform basic CRUD such as create,read,update and delete operations from the python classes. Has the database/connection.py to handle the database connection and provide cursor for executing sql commands.
The models/movies.py contains the movies class for managing movie records. The models/users.py contains the users class for managing the users accounts. The models/reviews.py contains the reviews class for managing movie reviews.
All the classes are responsible for managing records. They support basic CRUD functions and they all manage a dictonary (all) to store objects by their IDS.

## Database Management

- **Creating Tables:**

  - The `Movies`, `Users`, and `Reviews` classes include methods for creating and dropping tables.
  - Use the CLI to execute these methods and set up your database.

- **Populating the Database:**
  - Add initial data by calling the `create` method on each class or using the provided scripts.

### Example:

````python
from lib.model.movies import Movies

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
````

## How to Use

### Requirements for the installation requirements

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/luvley-dee48/phase-3-project-cli
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd phase-3-project-cli
   ```
3. **Install Dependencies:**
   ```bash
   pipenv install
   ```
4. **Activate the Virtual Environment:**
   ```bash
   pipenv shell
   ```
5. **Set Up the Database:**

   - Ensure SQLite is installed on your system.
   - Create the necessary tables by running the provided scripts or using the CLI to initialize them.

6. **Run the Application:**
   - You can start the application by running the `cli.py` or `__init__.py` script:
   ```bash
   python cli.py
   ```

## Technologies Used

- Python
- SQLite
- Pipenv

## Features

- Add, update, and delete movie records.
- Manage user accounts, including creating, updating, and deleting users.
- Post, update, and delete reviews for movies.
- View all movies and reviews.
- View all reviews by a specific user or for a specific movie.
- CLI

## Usage Instructions

1. **Starting the Application:**
   - After activating the virtual environment, run:
   ```bash
   python cli.py
   ```
2. **Main Menu:**

   - The main menu will present options to manage users, movies, or reviews.
   - Select an option by entering the corresponding number.

3. **Managing Users:**

   - To create a new user, select option `1` in the "Manage Users" menu and provide the required details.
   - To view all users, select option `2`.

4. **Managing Movies:**

   - To add a new movie, go to the "Manage Movies" section and select option `1`.
   - Update or delete movies using the respective options.

5. **Managing Reviews:**

   - View all reviews to see the feedback left by other users.

## Support and Contact Details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at:
<deborah.muoti@student.moringaschool.com>

## Licence

MIT License

Copyright (c) 2024 luvley-dee48

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
