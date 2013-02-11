import os
from jinja2 import Environment, FileSystemLoader

templatesdir = os.path.join(os.getcwd(), 'view/web/templates')

env = Environment(loader=FileSystemLoader(templatesdir))
