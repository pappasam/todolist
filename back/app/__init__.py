from flask import Flask
from config import config

# Force HTTPs or HTTP
def _force_preferred_protocol_wsgi(app, scheme):
    '''Force WSGI server to use the preferred url scheme'''
    def wrapper(environ, start_response):
        environ['wsgi.url_scheme'] = scheme
        return app(environ, start_response)
    return wrapper

def create_app(config_name):
    app = Flask(__name__)

    # Configure application from class object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Attach extensions
    from .extensions import ext
    for extension in ext.values():
        extension.init_app(app)

    from .views import resources
    for url, resource in resources.items():
        ext['api'].add_resource(resource, url)

    # Attach all Blueprints
    # from .services import blueprints_all
    # for blueprint in blueprints_all:
    #     app.register_blueprint(blueprint)

    # Force url_for to choose either http or https
    scheme = app.config['PREFERRED_URL_SCHEME']
    app.wsgi_app = _force_preferred_protocol_wsgi(app.wsgi_app, scheme)

    return app
