```python
import streamlit as st
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.scheduling import get_available_crew
from src.models import Base, ShipSchedule, Position, Person, Contract, Qualification

engine = create_engine('sqlite:///cruise-scheduler.db')
Base.metadata.bind = engine
DBSession = Session(bind=engine)

def main():
    st.title("Crew Scheduler")
    st.write("Welcome to the Crew Scheduler App. Please select the ship, month and position to get the list of available crew members.")

    ships = DBSession.query(ShipSchedule.ship).distinct().all()
    ship = st.selectbox('Select Ship', ships)

    months = DBSession.query(ShipSchedule.month).distinct().all()
    month = st.selectbox('Select Month', months)

    positions = DBSession.query(Position.name).distinct().all()
    position = st.selectbox('Select Position', positions)

    if st.button('Get Available Crew'):
        available_crew = get_available_crew(ship, month, position)
        st.write("Available Crew Members:")
        for crew in available_crew:
            st.write(crew.name)

if __name__ == "__main__":
    main()
```