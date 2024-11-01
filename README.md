# Todo List Project

A simple web application for managing a to-do list using Django.

## Description

The Todo List Project allows users to create, view, update, and delete tasks and mark them as completed or not
completed. Each task can have multiple tags for easier organization and filtering.

### Key Features

- **Home Page:** Displays a list of tasks with options to mark tasks as completed or not completed.
- **Tags Page:** Shows all tags with options to add, update, and delete them.
- **Create, update, and delete tasks and tags.**
- **Load sample data** using a JSON file.

## Setup and Installation

1. Clone the repository and navigate to the project folder:

   ```bash
   git clone git@github.com:arsen-arutiunov/todo-list.git
   ```

2. Install requirements:

    ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

    ```bash
   python manage.py migrate
   ```

4. Load sample data:

    ```bash
   python manage.py loaddata myapp_data.json
   ```

5. Start the server:

    ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser to view the site.

## Test user

A test user is available for logging in and exploring the app's functionality:
- **username**: `user`
- **password**: `user12345`

Use these credentials to log in and test the features.

## Project Structure
- **Home Page**: Contains the task list, buttons to create new tasks, edit, delete, and a button to toggle task completion status.
- **Tags Page**: Contains a list of tags, buttons to add new tags, edit, and delete them.

## Note
The project includes a sample data file, `myapp_data.json`, to load initial tasks and tags.
