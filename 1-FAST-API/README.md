# FastAPI API Development Notes

This repository contains notes and code snippets for developing APIs with FastAPI. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python-type hints.

## 1 - Setting Up Your Environment

To set up your environment for FastAPI development:

1. Install FastAPI and Uvicorn (ASGI server):

   ```bash
   pip install fastapi uvicorn


### Call the library FASTAPI app.

Install first your virtual environment and the libraries needed. 

    ```python
    from fastapi import FastAPI
  
    app = FastAPI()
    
### Start the development server.

    ```python
    uvicorn main:app --reload


### Basic pydantic structure for data validation.

    ```python
    from pydantic import BaseModel

    
    class PostSchema(BaseModel):
    title: str
    content: str

### 2 - Best Practices

 - Use Pydantic for Data Validation: Define Pydantic models to validate request and response data, ensuring the expected schema.

 - Consistent Status Codes: Use appropriate HTTP status codes (e.g., 201 for created resources, 404 for not found) to provide meaningful responses.

 - Automated Documentation: Take advantage of FastAPI's automatic documentation generation at /docs.

 - Folder Structure: Organize your project with a modular structure, including an app package with __init__.py and main.py.

 - Error Handling: Raise HTTPException for handling errors with detailed error messages and status codes.
