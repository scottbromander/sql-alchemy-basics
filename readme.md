# SQL Alchemy

- `pip install sqlalchemy`
- `python3 -m venv env` - creates the virtual environment
- `source ./env/bin/activate` - activates the venv
- `pip freeze > requirements.txt` - create requirements for the project, including sqlalchemy
- `models.py` - Typical pattern to create DB model in models.py

### Checking SQLLite
- `sqlite3 users.db`
- `.tables`
- `SELECT * FROM users;`