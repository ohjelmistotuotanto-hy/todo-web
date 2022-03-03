from database import db
from app import create_app

app = create_app()
app.app_context().push()


def create_tables():
    db.session.execute("""
        CREATE TABLE todos (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        );
    """)

    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS todos;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()
