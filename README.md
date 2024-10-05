# Django Project Setup

This guide provides instructions to set up a Django project using Python 3.10.

## Prerequisites

Make sure you have the following installed on your system:

- [Python 3.10](https://www.python.org/downloads/release/python-3100/) (including pip)
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended)

## Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>  
   cd <repository-directory>  
   ```

2. **Create a Virtual Environment**  
   It’s a good practice to create a virtual environment to manage your project dependencies.  
   ```bash
   python3.10 -m venv venv  
   ```

3. **Activate the Virtual Environment**  
   - **On Windows:**  
     ```bash
     venv\Scripts\activate  
     ```
   - **On macOS/Linux:**  
     ```bash
     source venv/bin/activate  
     ```

4. **Install Requirements**  
   Install the necessary packages listed in the `requirements.txt` file.  
   ```bash
   pip install -r requirements.txt  
   ```

5. **Run Migrations**  
   Apply migrations to set up your database.  
   ```bash
   python manage.py migrate  
   ```

6. **Create a Superuser (Optional)**  
   If you need access to the Django admin panel, create a superuser account.  
   ```bash
   python manage.py createsuperuser  
   ```

7. **Start the Development Server**  
   You can start the Django development server with the following command:  
   ```bash
   python manage.py runserver  
   ```  
   The server will start at `http://127.0.0.1:8000/` by default.

## Access the Application

Open your web browser and go to `http://127.0.0.1:8000/` to see your Django application in action.

### Admin Panel

To access the Django admin panel, navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

