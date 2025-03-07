#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    cities = session.query(City, State).filter(City.state_id == State.id)\
                    .order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
