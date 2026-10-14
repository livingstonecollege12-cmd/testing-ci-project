import pytest
from fastapi.testclient import TestClient
from main import app, books
client=TestClient(app)
@pytest.fixture(autouse=True)
def reset_state():
 books.clear()
 yield
 books.clear()
def test_health():
 r=client.get('/health'); assert r.status_code==200 and r.json()=={'status':'ok'}
def test_create_and_list_book():
 r=client.post('/books',json={'title':'Clean Code','author':'Robert C. Martin'}); assert r.status_code==201
 assert r.json()['title']=='Clean Code'; assert len(client.get('/books').json())==1
def test_blank_title_rejected():
 assert client.post('/books',json={'title':' ','author':'Writer'}).status_code==422
def test_mark_read_and_missing_book():
 book=client.post('/books',json={'title':'Book','author':'Writer'}).json()
 assert client.patch(f"/books/{book['id']}/read").json()['read'] is True
 assert client.patch('/books/999/read').status_code==404
