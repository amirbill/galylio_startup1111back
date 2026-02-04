# FastAPI Backend

## Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd back
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    - Windows (PowerShell):
        ```powershell
        .\venv\Scripts\Activate
        ```
    - Unix/MacOS:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Environment Variables:**
    Ensure you have a `.env` file in the `back` directory with your MongoDB credentials:
    ```
    MONGO_URI=mongodb+srv://...
    ```

## Running the Server

Start the development server with live reload:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:
- **API Root**: http://127.0.0.1:8000
- **Docs (Swagger UI)**: http://127.0.0.1:8000/docs
- **Redoc**: http://127.0.0.1:8000/redoc
