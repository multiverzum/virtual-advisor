# Virtual Advisor

## Installation Steps:

1. **Clone the project:** 
    ```
    git clone <project_repository_url>
    ```

2. **Create a new MySQL database.**

3. **Edit the `.env` file:** 
    - Update the database information with the details of the newly created MySQL database.

4. **Apply migrations:** 
    ```
    python manage.py makemigrations
    ```

5. **Migrate the database:** 
    ```
    python manage.py migrate
    ```

6. **Create a superuser:** 
    ```
    python manage.py createsuperuser
    ```

7. **Optional:** 
    - Make your user have admin privileges by loading the user table and setting `is_admin` to `1`.

8. **Run the app:** 
    ```
    python manage.py runserver
    ```

## Usage:
- After completing the installation steps, access the admin interface by navigating to `http://localhost:8000/admin/` in your web browser.
- Log in with the superuser credentials created in step 6 to start using the application.

