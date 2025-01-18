# Secure Login System with MongoDB Integration

## Project Overview
This project implements a secure login system using MongoDB as the database for storing usernames and hashed passwords. It provides a simple interface for user authentication and ensures data security through best practices like password hashing.

## Features
- User-friendly login page.
- Secure storage of credentials using MongoDB.
- Passwords are hashed for enhanced security.
- Scalable and efficient database integration.

## Prerequisites
- Python 3.8 or higher
- MongoDB (local or cloud instance)
- Required libraries:
  - `pymongo`
  - `bcrypt`
  - `streamlit` (if using a Streamlit interface)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Set up MongoDB:**
   - Configure a MongoDB instance (local or cloud) and create a database with a collection for storing user credentials.
   - Update the MongoDB connection string in the project code.

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Login Workflow:**
   - Users can register with a unique username and password.
   - Passwords are hashed using `bcrypt` before storage.
   - Login credentials are validated against the stored data in MongoDB.

## File Structure
- `app.py`: Main application file.
- `database.py`: Handles MongoDB interactions (e.g., storing and retrieving user data).
- `templates/`: Contains HTML templates (if using a web interface).

## Security Features
- Password hashing with `bcrypt` to protect stored credentials.
- Secure connection to MongoDB using appropriate authentication.
- Input validation to prevent SQL/NoSQL injection.

## Future Enhancements
- Add multi-factor authentication.
- Implement role-based access control.
- Integrate email verification for new users.
- Enhance the user interface for better usability.

---

Feel free to contribute to this project or provide feedback for further improvements!

