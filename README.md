# Code-Pilot – Assessment Management System

**Code-Pilot** is a backend assessment management system developed using Python, Django, Django REST Framework (DRF), and MySQL. It provides a structured platform for managing assessments, questions, student submissions, and answer evaluation through RESTful APIs.

The application supports separate student and administrator roles, authentication, role-based permissions, assessment scheduling, and manual evaluation of student submissions.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Application Modules](#application-modules)
- [Application Workflow](#application-workflow)
- [Authentication and Authorization](#authentication-and-authorization)
- [Assessment Scheduling](#assessment-scheduling)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Future Improvements](#future-improvements)

## Project Overview

Code-Pilot is designed to simplify the management of technical assessments.

Administrators can manage assessments and questions, while students can access assessments and submit their answers. Administrators can subsequently evaluate submissions by assigning marks and providing feedback.

The backend follows a modular Django architecture, with separate applications responsible for user management, assessments, questions, and evaluation.

## Key Features

### 1. User Management
- Custom Django user model.
- Separate student and administrator roles.
- User registration and authentication.
- Role-based access control.

### 2. Authentication
- JWT authentication using JSON Web Tokens.
- Django REST Framework token authentication.
- Protected API endpoints.
- Role-based permission handling.

### 3. Assessment Management
- Create and manage assessments.
- Store assessment details such as title, batch, programming language, exam date, start time, and duration.
- Maintain assessment status, including draft, published, and completed.
- Automatically calculate assessment end time.

### 4. Question Management
- Manage questions associated with assessments.
- Organize questions for different assessments.
- Maintain question-related information through APIs.

### 5. Student Submissions
- Provide APIs for student submissions.
- Manage submitted answers.
- Associate submissions and answers with the relevant assessment and student.

### 6. Manual Evaluation
- Administrators can evaluate student submissions.
- Assign marks to submitted answers.
- Provide feedback during evaluation.
- Maintain evaluation information.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Backend framework |
| Django REST Framework | REST API development |
| MySQL | Relational database |
| Django ORM | Database operations |
| JWT | Token-based authentication |
| DRF Token Authentication | API authentication |
| Git and GitHub | Version control |

## Application Modules

The project is divided into multiple Django applications.

| Module | Responsibility |
|---|---|
| `accounts` | Custom user model, registration, and authentication |
| `exams` | Assessment creation and scheduling |
| `problem` | Assessment question management |
| `evaluation` | Student submissions, answers, marks, and feedback |

This modular structure separates application responsibilities and makes the backend easier to maintain and extend.

## Application Workflow

1. Users register through the appropriate registration functionality.
2. Students and administrators access the system according to their assigned roles.
3. Administrators manage assessments and their scheduling.
4. Questions are associated with assessments.
5. Students access assessments and submit their answers.
6. Submission and answer records are maintained in the database.
7. Administrators evaluate submissions by assigning marks and feedback.

## Authentication and Authorization

Code-Pilot implements authentication and authorization using Django REST Framework.

**JWT Authentication**
- Supports token-based user authentication.
- Allows authenticated users to access protected APIs.

**DRF Token Authentication**
- Provides an additional token-based authentication mechanism.

**Role-Based Permissions**
- Separates student and administrator access.
- Restricts administrative operations according to user roles.

## Assessment Scheduling

The application includes assessment scheduling functionality.

Assessment scheduling considers:

- Assessment date.
- Starting time.
- Assessment duration.
- Automatically calculated ending time.

The ending time is calculated using the assessment's starting time and duration, helping maintain consistent scheduling information.

## Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python
- MySQL Server
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/Code-Pilot.git
```

### 2. Navigate to the Project Directory

```bash
cd Code-Pilot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create a MySQL database for the project.

Update the database configuration in the Django settings file with your database details:

- Database name
- Username
- Password
- Host
- Port

Do not commit database passwords or secret credentials to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## Future Improvements

- Add automated test coverage for API endpoints.
- Improve assessment reporting and performance analytics.
- Introduce automated evaluation capabilities.
- Add pagination and advanced filtering.
- Improve API documentation.

## Author

**Aravind Balaji K J**

[GitHub Profile](https://github.com/aravindbalaji4851-cmd)

[Project Repository](https://github.com/aravindbalaji4851-cmd/Code-Pilot)
