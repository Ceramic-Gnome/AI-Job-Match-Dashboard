from database.connection import engine, Base
from database import models


print("Creating database...")

Base.metadata.create_all(bind=engine)

print("Database created successfully!")