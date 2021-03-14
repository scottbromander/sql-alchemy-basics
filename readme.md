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

### Update
- Add a new user via command line: 
  - `$ python3`
  - `jethro = models.User(name='Jethro', fullname='Jethro Amendola', nickname='Bubba')`
- Update info:
  - `jethro.name = 'new name'`
  - Info stored in `models.session.new`, until committed
  - If you make an update to an entry post commit, you need `models.session.dirty`

### Rollbacks
- Rollbacks are like undos for sessions
- `jethro = models.session.query(models.User).filter(models.User.name=='Jethro').one()`
- `jethro.nickname = 'Bubbe'`
- `models.session.rollback()` - Undoes everything that is currently in session

### Delete
- `models.session.delete(jethro)`
- `models.session.commit()`