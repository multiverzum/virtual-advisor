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

6. **Optional:** 
    - Make your user have admin privileges by loading the user table and setting `is_admin` to `1`.

7. **Run the app:** 
    ```
    python manage.py runserver
    ```

## Usage:
- After completing the installation steps, access the admin interface by navigating to `http://localhost:8000/admin/` in your web browser.
- Create an account and login
- In the database make that user an admin by setting the column is_admin to 1

