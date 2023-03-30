"""
1. Create a main project directory
2. For every project use venv which is virtual environment and install separate specific
versions for specific projects.
3. activate the virtual environment and install flask
4. Create a package(folder) named "app" 
5. Inside app/ create __init__.py file
6. Application exists in a package
7. In python a subdirectory which contains __init__.py file is considered as package and can be imported
8. When we import a package __init__.py executes and defines what symbols exposes to world 
Now in __init__.py file import flask
"""

from flask import Flask

# Configure flask
# here app is a variable defined as insance of class Flask.
# which makes it member of app package
app = Flask(__name__) 


# here 'app' referes to 'app' package defined by 'app' directory and __init__.py script
# To avoid circular import import routes below app
from app import routes 