"""Main module."""
from flask import Flask
from routes.index import register_routes  # type: ignore # Import function that registers routes

app = Flask(__name__)
register_routes(app)  # Register all your routes here

if __name__ == '__main__':
    app.run(host='localhost', port=5500, debug=True)
