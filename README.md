# Productivity App

This is a simple productivity app built with Flask. It allows users to manage their tasks efficiently and stay organized.

## Features

- Task Management: Organize your tasks with our intuitive task management system.
- Time Tracking: Keep track of the time you spend on each task to improve efficiency.
- Analytics: Analyze your productivity with detailed reports and insights.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Aniket-Chinchankar/ToDo.git
    cd ToDo
    
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure
