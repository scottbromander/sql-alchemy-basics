from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# in production, that would be the url, here this is local. Echo adds info
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()

# model is the table and columns

class User(Base):
    # Set the table name
    # When creating a new table, you need to at least create a name and primary key
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)