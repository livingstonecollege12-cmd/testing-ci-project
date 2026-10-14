from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app=FastAPI(title='Reading List API')
books={}; next_id=1
class BookIn(BaseModel):
 title: str=Field(min_length=1,max_length=160)
 author: str=Field(min_length=1,max_length=120)
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/books')
def get_books(): return list(books.values())
@app.post('/books',status_code=201)
def add_book(book:BookIn):
 global next_id
 item={'id':next_id,'title':book.title.strip(),'author':book.author.strip(),'read':False}; books[next_id]=item; next_id+=1; return item
@app.patch('/books/{book_id}/read')
def mark_read(book_id:int):
 if book_id not in books: raise HTTPException(404,'Book not found')
 books[book_id]['read']=True; return books[book_id]
