```python
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShipSchedule(Base):
    __tablename__ = 'ship_schedules'

    id = Column(Integer, primary_key=True)
    ship_name = Column(String)
    month = Column(String)
    position_id = Column(Integer, ForeignKey('positions.id'))

    position = relationship('Position', back_populates='schedules')

class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    qualification_id = Column(Integer, ForeignKey('qualifications.id'))

    qualification = relationship('Qualification', back_populates='positions')
    schedules = relationship('ShipSchedule', back_populates='position')

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    qualification_id = Column(Integer, ForeignKey('qualifications.id'))

    qualification = relationship('Qualification', back_populates='people')

class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    start_date = Column(Date)
    end_date = Column(Date)

    person = relationship('Person', back_populates='contracts')

class Qualification(Base):
    __tablename__ = 'qualifications'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    positions = relationship('Position', back_populates='qualification')
    people = relationship('Person', back_populates='qualification')
```