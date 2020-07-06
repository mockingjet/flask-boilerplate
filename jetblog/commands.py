import os
import click


import alembic.config
from jinja2 import Template
from flask.cli import AppGroup, with_appcontext
from sqlalchemy.exc import IntegrityError

from . import seeds
from .database import engine, Model
from .utils import print_exception

db = AppGroup('db')
seed = AppGroup('seed')
make = AppGroup('make')


@db.command('reset')
def db_reset():
    """ reset all tables """
    alembic.config.main(argv=['downgrade', 'base'])
    alembic.config.main(argv=['upgrade', 'head'])
    alembic.config.main(argv=['revision', '--autogenerate'])
    alembic.config.main(argv=['upgrade', 'head'])


@db.command('migrate')
def db_migrate():
    alembic.config.main(argv=['revision', '--autogenerate'])


@db.command('upgrade')
def db_upgrade():
    alembic.config.main(argv=['upgrade', 'head'])


@db.command('merge')
def db_merge():
    alembic.config.main(argv=['merge'])


@seed.command('articles')
@with_appcontext
@print_exception(IntegrityError)
def seed_articles():
    seeds.create_articles()
    print("creating articles --- done")


@make.command('module')
@click.option('--app', help="The application name, default=root dirname", default=os.path.relpath('.', '..'))
@click.option('-mod', '--module', prompt=True, help="The module name and table name")
@click.option('-m', '--model', prompt=True, help="The model name and table id name (+'_id')")
def make_module(app, module, model):
    dirname = os.path.join(app, 'modules', module)
    try:
        os.makedirs(dirname)
    except FileExistsError as e:
        print(str(e))
        exit()

    # write into {{app}}/{{module}}/__init__.py
    init_path = os.path.join(dirname, '__init__.py')
    with open(init_path, 'w') as file:
        output = Template("from . import views").render()
        file.write(output)

    # make models.py
    models_template_path = os.path.join(
        app, '.mustaches', 'models.py.mustache')
    with open(models_template_path) as file:
        template = Template(file.read())

    # write into {{app}}/{{module}}/models.py
    models_path = os.path.join(dirname, 'models.py')
    with open(models_path, 'w') as file:
        output = template.render(
            app=app, model=model, table=module, id=model.lower() + '_id')
        file.write(output)

    # make views.py
    views_template_path = os.path.join(
        app, '.mustaches', 'views.py.mustache')
    with open(views_template_path) as file:
        template = Template(file.read())

    # write into {{app}}/{{module}}/views.py
    views_path = os.path.join(dirname, 'views.py')
    with open(views_path, 'w') as file:
        output = template.render(
            app=app, model=model, module=module)
        file.write(output)
