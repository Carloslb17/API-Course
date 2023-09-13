from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
#https://www.youtube.com/watch?v=0sOvCWFmrtA

# 1:00

app = FastAPI()


class Post(BaseModel): # SCHEMA
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

myposts = [{"title":"title post", 
            "content": "content 1",
            "id": 1},
            {"title":"title post", 
            "content": "content 2",
            "id": 2

}]

def find_post(id):
    for p in myposts:
        if p['id'] == id:
             return p
        

def find_indexpost(id):
    for i, p in enumerate(myposts):
        if p['id'] == i:
             return p

@app.get("/") # Decorator
#async
def root(): # Function
    return {"message": "Hello World"}




@app.get("/posts", status_code=status.HTTP_201_CREATED)
def get_posts():
    return {"data": myposts}


@app.get("/createposts")
def create_posts(post: Post): #Referencing the Post pydantic model will the check and validate the type of content if not will send an error,
    print(post.dict())
    
    myposts.append(post.model_dump())
    return {"data": Post}



@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"NOT found {id}")
        
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post wit"} 
    return {"data": post}

@app.delete("/posts/{id}",  status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    #deleting post
    index = find_indexpost(id)
    myposts.pop(index)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Does not exist {id}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}") #,  status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post: Post):
    
    index = find_indexpost(id)
    myposts.pop(index)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Does not exist {id}")



    post_dict = post.model_dump()
    post_dict['id'] = id
    myposts[index] = post_dict
    
    
    return {"message": "updated"}