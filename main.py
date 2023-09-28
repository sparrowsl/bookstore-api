from fastapi import FastAPI

app = FastAPI()


books = ["Harry Potter", "Chronicles of Narnia",
         "Atomic Habits", "Learning Python", "Learning Go"]


@app.get("/")
async def home():
    return {"message": "Welcome to bookstore!"}


@app.get("/books")
async def get_books():
    return {"books": books}


@app.get("/books/{index}")
async def get_book(index: int):
    if index not in range(1, len(books) + 1):
        return {"message": "No book found"}

    return {"book": books[index - 1]}
