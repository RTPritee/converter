# JSON to CSV Converter

This project provides functionality for converting `.json` files to `.csv` format. The primary focus is to handle missing values in the JSON files during the conversion process.

## Features

1. **Login and Authentication**  
   - Users log in using their credentials.  
   - After login, they are redirected to the Landing Page.

2. **Upload File**  
   - On the File Upload Page, users can upload a `.json` file.  
   - The file is sent to the FastAPI `/convert` endpoint for processing.

3. **Download CSV**  
   - The converted CSV file is returned as a response and automatically downloaded by the user.

4. **Error Handling**  
   - Appropriate error messages are displayed if:  
     - No file is uploaded.  
     - Communication with the FastAPI server fails.

---

## How to Run the Project

### FastAPI Backend

1. **Activate Virtual Environment**  
   ```bash
   source venv/Scripts/activate
   ```

2. **Install Requirements**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Application**  
   ```bash
   uvicorn main:app --reload
   ```

### Django Project

1. **Activate Virtual Environment**  
   ```bash
   source venv/Scripts/activate
   ```

2. **Install Requirements**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Superuser**  
   ```bash
   python manage.py createsuperuser
   ```  
   Provide the username and password.

4. **Apply Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Django Server**  
   ```bash
   python manage.py runserver 8081
   ```

---

## Screenshots

### 1. Login Page  
![1](https://github.com/user-attachments/assets/cc98502a-785a-45dc-b3e7-bfdb445208ff)

### 2. File Upload Page  
![2](https://github.com/user-attachments/assets/42717140-6250-4203-a42a-1af2aa7623ff)
