# User Documentation


# Install dependencies 
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirement.txt
```

# run the local server
```bash
python manage.py runserver
```

# Add a application
- http://localhost/o/application
- put the necessary details.


# for generate the access_token and refresh_token
 In Postman body provide these.
{
    "grant_type": "password",
    "username": "your_username",
    "password": "your_password",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
}

In response access_token would be generate.

# Access the protected data using the access_token
Using the Postman in header Authorization  Bearer <your_access_token>

in the get method access the view using this url in postman, http://localhost:8000/myapp/api_protected/.
