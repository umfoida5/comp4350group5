from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('view/web/templates'))
