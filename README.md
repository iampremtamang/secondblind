# Book Inventory Management System

## Overview

The **Book Inventory Management System** is a Django-based web application designed to manage a collection of books. It allows users to perform CRUD operations (Create, Read, Update, Delete) on books, filter the inventory based on various criteria, and export book data in CSV format.

## Features

- Add new books to the inventory
- Filter books by title, author, genre, and publication date
- Export book data to CSV
- Responsive user interface

## Tech Stack

- **Backend**: Django
- **Database**: SQLite (can be switched to MySQL/PostgreSQL)
- **Frontend**: HTML, CSS (with Bootstrap)
- **Export Formats**: CSV

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (optional but recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/iampremtamang/secondblind.git
cd secondblind
```

### 2. Create and Activate a Virtual Environment

#### Create virtual environment
```bash
python -m venv env
```

#### Activate virtual environment (Linux/macOS)
```bash
source env/bin/activate
```
    
#### Activate virtual environment (Windows)
```bash
source .\env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Migrate the database to create the required tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Running the Application
To start the development server, run the following command:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser to view the application.
