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

## 2 - Best Practices

 - Use Pydantic for Data Validation: Pydantic models validate requests and response data, ensuring the expected schema. This will allow you to check the data passed to your API.

 - Consistent Status Codes: It is really useful to use appropriate HTTP status codes (e.g., 201 for created resources, 404 for not found) in order to provide meaningful responses. This will allow the user a complete understanding when using the API. 

 - Automated Documentation: FastAPI creates automatic documentation generation at "server"/docs meanwhile in POSTMAN all the documentation needs to be created manually. 

 - Folder Structure: It is a must to organize your project with a modular structure, including an app package with __init__.py and main.py in order to 

 - Error Handling: Raise HTTPException for handling errors with detailed error messages and status codes.
