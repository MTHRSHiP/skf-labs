from db.db import comments, users
from uuid import uuid4


def seed_db():
    init_users = ["Admin", "John"]
    # Seed the database with some users
    if(users.count() == 0):
        new_users = [
            {"_id": uuid4().hex,
             "username": init_users[0], "password": "07RYbe$!9y11"},
            {"_id": uuid4().hex,
             "username": init_users[1], "password": "07RYbe$!9y22"}
        ]
        users.insert_many(new_users)

        # Seed the database with some comments
        if(comments.count() == 0):
            new_comments = [
                {"_id": uuid4().hex, "author": init_users[0],
                 "text": "Good picture!"},
                {"_id": uuid4().hex, "author": init_users[1], "text": "Nice!"}
            ]

            comments.insert_many(new_comments)
