# Project Title

This project is a simple FastAPI application that provides student information through an API endpoint.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Anuoluwapo25/HNG-Stage0
}
    cd HNG-Stage0
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
    

4. **Run the application**:
    ```
    python manage.py runserver
    ```

## API Documentation

### Endpoint URL

- **GET** `/`

### Response Format

- **Response**:
    ```json
    {
        "data":{
                  "email": "anuoluwapoali25@gmail.com",
                  "current_datetime": "2025-01-31T09:23:18.721779+00:00",
                  "github_url": "https://github.com/Anuoluwapo25/HNG-Stage0"
           },
        
    ```

### Example Usage

To get the user information, send a GET request to the `/` endpoint. You can use `curl` or any API client like Postman.

```sh
curl -X GET "http://127.0.0.1:8000/api"
```

