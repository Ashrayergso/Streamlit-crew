```python
import pandas as pd
from sqlalchemy import create_engine
from models import Base, ShipSchedule, Position, Person, Contract, Qualification

def load_data():
    engine = create_engine('sqlite:///cruise-scheduler.db')
    Base.metadata.create_all(engine)

    # Load ShipSchedule data
    df = pd.read_csv('data/ship_schedule.csv')
    df.to_sql('ship_schedule', engine, if_exists='replace', index=False)

    # Load Position data
    df = pd.read_csv('data/position.csv')
    df.to_sql('position', engine, if_exists='replace', index=False)

    # Load Person data
    df = pd.read_csv('data/person.csv')
    df.to_sql('person', engine, if_exists='replace', index=False)

    # Load Contract data
    df = pd.read_csv('data/contract.csv')
    df.to_sql('contract', engine, if_exists='replace', index=False)

    # Load Qualification data
    df = pd.read_csv('data/qualification.csv')
    df.to_sql('qualification', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    load_data()
```