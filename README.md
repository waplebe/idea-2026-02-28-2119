# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. The frontend provides a basic interface for interacting with the API.

**Why it's useful:**

A task manager is a fundamental tool for productivity. This API provides a foundation for building more complex task management applications or integrating task management functionality into existing systems.

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  **Set up the frontend:**
    ```bash
    npm install
    npm start
    ```

4.  **Set environment variables:**
    Create a `.env` file in the root directory and populate it with the following:
    ```
    DATABASE_URL=sqlite:///tasks.db
    ```

**Running the application:**

1.  **Backend:**
    ```bash
    python app.py
    ```

2.  **Frontend:**
    The frontend should automatically launch in your browser after running `npm start`.  It will typically open at `http://localhost:5173`.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `PUT /tasks/{id}`: Updates an existing task. Request body should be a JSON object with the fields to update.
*   `DELETE /tasks/{id}`: Deletes a task.

**Example Usage:**

*   **Create a task:**
    `curl -X POST -H "Content-Type: application/json" -d '{"title": "Grocery Shopping", "description": "Buy milk, eggs, and bread"}' http://localhost:5000/tasks`

*   **Get all tasks:**
    `curl http://localhost:5000/tasks`

*   **Get a specific task:**
    `curl http://localhost:5000/tasks/1`

**New Features:**

*   **Add Task Functionality:**  The frontend now includes a button to add new tasks.  When clicked, it prompts the user for a title and description, sends a POST request to the `/tasks` endpoint, and then refreshes the task list to display the new task.
*   **Error Handling:** Added basic error handling to the POST request for creating tasks.  If the title is missing, an error message is displayed.
*   **Environment Variables:** Uses `dotenv` to load environment variables from a `.env` file.

**Testing:**

The `tests/test_app.py` file contains unit tests for the API endpoints.  Run the tests using `pytest`.