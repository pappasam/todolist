from collections import OrderedDict
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
ext = OrderedDict()
ext['db'] = SQLAlchemy()
