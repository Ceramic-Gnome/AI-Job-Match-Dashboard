from database.connection import Base, engine
from database.models import Job  # noqa: F401

print("Creating database...")

Base.metadata.create_all(bind=engine)

print("Database created successfully!")
