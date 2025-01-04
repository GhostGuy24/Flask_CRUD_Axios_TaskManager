# Flask Task Manager

## Overview
The Flask Task Manager is a web-based application designed to manage tasks efficiently. Users can create, read, update, delete, and mark tasks as completed. The project leverages Flask for backend functionality and integrates Axios for seamless API requests.

---

## Features

1. **Task Creation**:
   - Users can add new tasks with a name, description, and deadline.
2. **Task Viewing**:
   - Display all tasks with their details.
   - Separate tasks based on their completion status.
3. **Task Update**:
   - Edit existing tasks.
   - Update task details (name, description, deadline, and completion status).
4. **Task Deletion**:
   - Remove tasks from the list.
5. **Mark as Completed**:
   - Toggle the completion status of tasks using the update endpoint.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2
- **HTTP Client**: Axios
- **Database**: In-memory Python list (for simplicity)

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GhostGuy24/Flask_CRUD_Axios_TaskManager.git
   cd flask-task-manager
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the Flask application:
    ```bash
    Flask run
4. Access the application in your browser:
    ```bash
    http://127.0.0.1:5000/
    
