Project Overview
----------------------
Flask based cloud storage via session, JWT  

### Installation
  ```python 
      python -m venv venv 
      ---------------
      venv/scripts/activate
      ---------------
      pip install -r requirements.txt 
      ---------------
      flask db init
      flask db migrate  #adding models in database
      flask db upgrade
      ---------------
      py run.py 
  ```
  
    
----------------------


### Features

1. User Authentication
    via Flask-Login, Flask-Bcrypt, and Flask-JWT-Extended

    - User Registration: Users can register by providing a name and password. The password is hashed using Flask-Bcrypt before being stored in the database.
   
    - User Login: Users can log in by providing their name and password. The provided password is hashed and compared with the stored hashed password in the database. If the passwords match, the user is authenticated and logged in using Flask-Login.
   
    - User Logout: Simple handler for logout
   
    - Token-Based Authentication: For additional security, you can use Flask-JWT-Extended to implement token-based authentication. When a user logs in, a JWT token is generated and returned to the client. The client can then include the token in subsequent requests to authenticate themselves. Flask-JWT-Extended verifies the token and allows access to protected routes.

  
2. Secure Data Storage

    Models:
    
     - User: Stores user information.
    
     - Object: Represents uploaded files with metadata such as filename, user ID, and file data.
    
    Database:
    
     - Uses SQLAlchemy for ORM, Flask-Migrate for database management.
    
     - SQLite as the default storage backend.
    
    Strict Data Control:
    
     - Only the user who uploaded a file can delete it.

3. File Management

      - Upload Files: Users can upload files, which are stored in the database.
      
      - Download Files: Users can download files via a unique link.
      
      Security Considerations

        - Password Hashing: All passwords are securely hashed before storage.
        
        - JWT Authentication: Tokens ensure secure access to protected resources.
        
        - Session Management: Users remain logged in via Flask-Login.
        
        - File Access Control: Only file owners can delete their uploads.


   ### Authentication Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/register` | GET, POST | Register a new user |
| `/login` | GET, POST | Authenticate and log in |
| `/logout` | GET, POST | Log out the user |

### File Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/` | GET, POST | Upload and list files |
| `/download/<upload_id>` | GET | Download a file |
| `/delete/<upload_id>` | GET, POST | Delete a file (only by uploader) |

        
Tech part
----------------------
Backend

    Flask - Web framework
    
    Flask-Login - Manages user sessions and authentication
    
    Flask-Bcrypt - Hashes passwords securely
    
    Flask-JWT-Extended - Provides token-based authentication
    
    SQLAlchemy - ORM for database operations

Frontend

    Bootstrap - Styling framework
    
    HTML/CSS - Basic UI components
