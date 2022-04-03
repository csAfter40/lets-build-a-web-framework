from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update, delete, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)
    greet_count = Column('count', Integer, default=0)

engine = create_engine('sqlite:///project.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

def create_counter(username):
    with Session() as session:
        try:
            counter = User()
            counter.username = username
            session.add(counter)
            session.commit()
        except IntegrityError:
            session.rollback()
            session.close()

def increase_count(username):
    with Session() as session:
        session.execute(
        update(User).
        where(User.username == username).
        values(greet_count=User.greet_count + 1)
        )
        session.commit()

def get_count(username):
    count = 0
    with Session() as session:
        object = session.execute(
        select(User).
        where(User.username == username)
        ).scalars().first()
        count = object.greet_count
        session.commit()
    return count