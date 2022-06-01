# The One Piece API

Open source RESTful API project based in "One Piece" anime, using Flask micro-framework.

## Requirements:

- **FLask Restful**: It's an extention that allows to generate RESTf APIs very easily. Also, it comes with a lot of functionalities.
- **Flask SQLAlchemy**: To interact with the database through its ORM.
- **Flask Migrate**: This extention allows to generate the database tables from migration files.
- **Flask Marshmallow**: It's an extention that makes it easy to serialize models from the database to JSON and vice versa.
- **Marshmallow SQLAlchemy**: To integrate Flask  Marshmallow with SQLAlchemy.

Execute this command to install all the extentions and dependencies.

```
pip install flask flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow-sqlalchemy
```