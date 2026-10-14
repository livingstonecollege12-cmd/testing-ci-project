# Reading List API + Automated Tests
Small FastAPI service demonstrating input validation, error handling, pytest, and GitHub Actions CI.

Run tests:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```
Run server with ` .\.venv\Scripts\python.exe -m uvicorn main:app --reload`.

Limitation: data is held in memory and resets on restart. Use a database for a real app.
