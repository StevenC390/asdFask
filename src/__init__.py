from flask import Flask
from os import environ
from src.database import db, ma, migrate
from src.endpoints import products, users, houses

def create_app():
    app = Flask(__name__,
                instance_relative_config=True)
    
    app.config['ENVIRONMENT'] = environ.get("ENVIRONMENT")
    config_class = 'config.DevelopmentConfig'
    
    match app.config['ENVIRONMENT']:
        case "development":
            config_class = 'config.DevelopmentConfig'
        case "production":
            config_class = 'config.ProductionConfig'
        case _:
            print(f"ERROR: environment unknown: {app.config.get('ENVIRONMENT')}")
            app.config['ENVIRONMENT'] = "development"
                
    app.config.from_object(config_class)
    
    ##Load the blueprints (endpoints)
    app.register_blueprint(products)
    app.register_blueprint(users)
    app.register_blueprint(houses)
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    ## Create the database tables
    with app.app_context():
        db.drop_all()
        db.create_all()
    return app