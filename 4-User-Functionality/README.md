# Object-Relational Mapping (ORM) with SQLAlchemy

Welcome to the Object-Relational Mapping (ORM) example using SQLAlchemy! This repository demonstrates how to use SQLAlchemy to interact with a relational database in a Python application.

## Table of Contents
- [Introduction to ORM](#introduction-to-orm)
- [Installation](#installation)
- [Usage](#usage)

## Introduction to ORM

ORM stands for Object-Relational Mapping, a technique that allows developers to interact with relational databases using object-oriented programming languages. It bridges the gap between the object-oriented world of Python and the relational world of databases, making it easier to work with databases in your application.

### Key Benefits of ORM:
- **Abstraction**: ORM provides a higher-level, more abstract way to interact with the database, reducing the need to write raw SQL queries.
- **Database Independence**: You can switch between different database systems (e.g., SQLite, MySQL, PostgreSQL) without changing your application code.
- **Improved Productivity**: ORM simplifies database operations, leading to faster development and maintenance of applications.
- **Object-Oriented Approach**: You can work with database records as objects, making the code more readable and maintainable.

## Installation

- To get started with this example, you'll need to have Python and SQLAlchemy installed. If you haven't already, you can install them using pip:

    ```bash
    pip install sqlalchemy


## Usage
In this repository, you'll find a Python script (main.py) that demonstrates the usage of SQLAlchemy for ORM. We'll use SQLite as our database for this example.

 - Define Models: In the models.py file, define your database tables as Python classes. For example:


    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    
    Base = declarative_base()
    
    class User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        username = Column(String)
        email = Column(String)
        
- Create a Session: In main.py, create a SQLAlchemy session to interact with the database:

    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

-  Create an SQLite database in memory (you can change this to a file-based database)

    ```python
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
 - Perform Database Operations: Use the session to perform CRUD operations on your models. Example:

    ```python
    #Create a new user
    new_user = User(username='john_doe', email='john@example.com')
    session.add(new_user)
    session.commit()

    # Query all users
    users = session.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")




## Retrieving data from a post. 

- The following code is an example of how you can retrieve data from a database using an ORM initiated above, without using any type of SQL. The reason is that the ORM transforms the Python language into SQL with some methods. 

    ```python    
    @app.get("sqlalchemy")
    def test_posts(db: Session = Depends(get_db)):
        post = db.query(models.Post).all()
        return {"success": post}

## Differences between a Schema pydantic model and the schema of the database SQLAlchemy.
- The schema from <b> Pydantic </b>  defines the structure of a request or a response. This will ensure a pre-defined shape for the user who wants to use our API and also provide validation. The following code is an example od using pydantic and inheritance
  
    ```python
    # A good practice will be based on creating a class base as a parent.
    class PostBase(BaseModel):
        title: str
        content: str
        published: bool = True

    class CreatingPost(PostBase)
        pass

    class Post(PostBase)
        id: int
        created_at: time

        class Config:
            orm_mode = True
  
- The schema from <b> SQLAlchemy </b> is responsible for defining the variables or columns of our database. Is used to query, create, delete, and update entries. 
    

