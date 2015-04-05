__author__ = 'Hanz'
from flask_script import Manager
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)

bootstrap = Bootstrap(app)

if __name__=='__main__':
    manager.run()
