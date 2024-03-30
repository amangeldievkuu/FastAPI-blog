from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []


# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# Get single todo
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todo found"}


# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}


# Update a todo
@app.put("/todo/{todo_id}")
async def create_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_object.id
            todo.item = todo_object.item
            return {"todo": todo}
    return {"message": "No todos was found to update"}


# Delete a todo
@app.delete("/todos/{todo_id}")
async def del_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo has been deleted"}
    return {"message": "No todo was found"}