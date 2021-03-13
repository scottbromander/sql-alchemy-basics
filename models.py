from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# in production, that would be the url, here this is local. Echo adds info
engine = create_engine('sqlite:///users.db', echo=False)
# Binds our sessions to the database
Session = sessionmaker(bind=engine)
session = Session()
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

    # Just created. Not added to the database yet
    # scott_user = User(name='Scott', fullname='Scott Bromander', nickname='Bromander')
    # print(scott_user.name)
    # print(scott_user.id)
    # # Stages, but not committed to the database yet
    # session.add(scott_user)
    # # Adds our user to the database
    # session.commit()
    # print(scott_user.id)

    # Adding multiple entries at once, using add_all
    # session.add_all([
    #     User(name='Jackson', fullname='Jackson Bromander', nickname='Jack'),
    #     User(name='Rachael', fullname='Rachael Bromander', nickname='Rach'),
    #     User(name='Scott', fullname='Scott Bromander', nickname='Bromander')
    # ])

    # Here we are breaking it across multiple users
    new_users = [
        User(name='Jackson', fullname='Jackson Bromander', nickname='Jack'),
        User(name='Rachael', fullname='Rachael Bromander', nickname='Rach'),
        User(name='Scott', fullname='Scott Bromander', nickname='Bromander')
    ]

    session.add_all(new_users)
    session.commit()

    for user in new_users:
        print(user.fullname, user.id)