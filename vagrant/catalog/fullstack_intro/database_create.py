from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Honey's Coffee")
session.add(myFirstRestaurant)
session.commit()

"C:\Users\mateo\Documents\programming\udacity\fullstack_intro"