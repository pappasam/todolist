from collections import OrderedDict
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Initialize extensions
ext = OrderedDict()
ext['db'] = SqlAlchemy()
ext['api'] = Api()
