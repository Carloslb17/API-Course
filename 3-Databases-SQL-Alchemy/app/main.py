from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import time
import models
from database import *
from sqlalchemy.orm import Session
#Database connection
import psycopg2
from psycopg2.extras import RealDictCursor


import sys
print(sys.path)

#https://www.youtube.com/watch?v=0sOvCWFmrtA


models.Base.metadata.create_all(bind=engine)      # This will looks if there is a table in the database and will be create one if there isn't.
app = FastAPI()




class Post(BaseModel): # SCHEMA
    title: str
    content: str
    published: bool = True
   


# The connections ot the database may fail so let's include a try operator. Docs ---> https://www.psycopg.org/docs/install.html
while True:
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host = 'localhost', database='fastapi', port="5432",
                                user='postgres', password='admin',
                                cursor_factory= psycopg2.extras.RealDictCursor #Makes a dictionary
                                )   # Enviroment variables pls

        # Open a cursor to perform database operations
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
        # Execute a query
        #cur.execute("SELECT * FROM my_data")
        # Retrieve query results
        #records = cur.fetchall()

    except Exception as error:
        print("Connetction to Database failed")
        print("Error: ", error)
        time.sleep(3)

myposts = [{"title":"title post", 
            "content": "content 1",
            "id": 1},
            {"title":"title post", 
            "content": "content 2",
            "id": 2

}]


### --------------- Functions -------------

def find_post(id):
    for p in myposts:
        if p['id'] == id:
             return p
        

def find_indexpost(id):
    for i, p in enumerate(myposts):
        if p['id'] == i:
             return p




### --------------- Decorators -------------

@app.get("/") # Decorator
#async
def root(): # Function
    return {"message": "Hello World"}


@app.get("sqlalchemy")
def test_posts(db: Session = Depends(get_db)):


    return {"success"}

@app.get("/posts", status_code=status.HTTP_200_OK)
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    cursor.fetchall
    new_post = cursor.fetchone()
    return {"post included": new_post}


### SQL Injection - manipulate data within a database. 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)""", 
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}



@app.get("/posts/{id}") 
def get_post(id: int): # We validate as a number cause the uer can type some type of string, then we convert into str to fetch the data from the database. 
    cursor.execute(""" SELECT * from posts WHERE id = %s""", (str(id))) # Extra comma cause might lead to some issues. 
    post = cursor.fetchone()
    conn.commit()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id was not found {id}")

    return {"data": post}



@app.delete("/posts/{id}",  status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    cursor.execute(""" DELETE FROM posts WHERE id = %s returning *""", (str(id),)) # Extra comma cause might lead to some issues. 
    deleted_post = cursor.fetchone()
    conn.commit() # Every time we make a change to a database remember to coomit same as git.
    
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Does not exist {id}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}") #,  status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post: Post):
    
    cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s RETURNING *""", 
                   (post.title, post.content, post.published)) # Extra comma cause might lead to some issues. 
    updated_post = cursor.fetchone()
    conn.commit() # Every time we make a change to a database remember to coomit same as git.


    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id was not found{id}")
    
    return {"message": updated_post}