import os

path_this = os.path.dirname(os.path.abspath(__file__))

class ConfigBase(object):
    DEBUG = True
    PORT = 5000
    HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(path_this, 'notes.db')
    )

    def init_app(self):
        pass

config = {
    'base': ConfigBase,
    'default': ConfigBase,
}
