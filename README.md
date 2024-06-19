# FastAPI Application

This is a FastAPI application that includes a health check endpoint and a router for summarization.

## Requirements

- Python ^3.12
- `pip` (Python package installer)

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://https://github.com/AndrewCheUA/JuniorTestTask.git
    cd JuniorTestTask
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server:**

    ```sh
    uvicorn main:app --host localhost --port 8000 --reload
    ```

2. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`.

3. **Health Check Endpoint:**

    You can check the health of the application by navigating to `http://localhost:8000/api/healthchecker`.

## Project Structure

- `main.py`: The main entry point of the application.
- `app/routes/lcresponse.py`: Contains the routes for summarization.
- `config.py`: Configuration settings for the application.

## Additional Information

- **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Uvicorn Documentation:** [https://www.uvicorn.org/](https://www.uvicorn.org/)

