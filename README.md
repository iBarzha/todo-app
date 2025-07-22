# Todo App

A Django-based task management application that allows users to create, manage, and track tasks with subtasks.

## Features

- Create and manage tasks
- Add subtasks to main tasks
- Track task status (Not Started, In Progress, Completed)
- Clean and responsive web interface
- SQLite database for data persistence

## Project Structure

```
todo-app/
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
├── todo_app/             # Main Django project
│   ├── settings.py       # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
└── tasks/               # Tasks Django app
    ├── models.py        # Task and Subtask models
    ├── views.py         # View logic
    ├── urls.py          # App URL routing
    ├── forms.py         # Django forms
    ├── templates/       # HTML templates
    └── static/          # CSS and JS files
```
