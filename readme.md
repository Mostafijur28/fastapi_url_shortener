# FastAPI URL Shortener

This project implements a simple URL shortener service using FastAPI. Below are the steps to install, run, and test the application.

---

## Requirements

- **Python 3.8+**
- **pip** (Python package manager)

---

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourUsername/fastapi_url_shortener.git
   cd fastapi_url_shortener
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```bash
   python -c "from database import init_db; init_db()"
   ```

---

## Running the Application

1. **Start the Server**
   ```bash
   uvicorn main:app --reload
   ```

   The application will run at `http://127.0.0.1:8000`.

2. **Access API Documentation**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Execution Steps

### 1. **Shorten a URL**
- **Endpoint**: `POST /shorten`
- **Payload**:
  ```json
  {
      "original_url": "https://example.com",
      "expiry_hours": 24
  }
  ```
- **Response**:
  ```json
  {
      "shortened_url": "http://short.ly/abc123",
      "expiration_time": "2025-01-23T12:34:56Z"
  }
  ```

### 2. **Redirect to the Original URL**
- **Endpoint**: `GET /{short_url}`
- **Example**: `http://127.0.0.1:8000/abc123`
- **Behavior**:
  - Redirects to the original URL if valid.
  - Returns `404` if the URL is expired or not found.

### 3. **Retrieve Analytics**
- **Endpoint**: `GET /analytics/{short_url}`
- **Example**: `http://127.0.0.1:8000/analytics/abc123`
- **Response**:
  ```json
  {
      "shortened_url": "abc123",
      "access_count": 5,
      "access_logs": [
          {
              "ip_address": "192.168.1.10",
              "timestamp": "2025-01-22T12:00:00Z"
          },
          {
              "ip_address": "192.168.1.11",
              "timestamp": "2025-01-22T12:05:00Z"
          }
      ]
  }
  ```

