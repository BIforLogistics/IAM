import logging
import click
import pkg_resources
from configs.flask_config import APP

@click.group()
def web():
    """Group all commands here"""
    pass

@click.command()
def version():
    """Displays the current build version"""
    version = pkg_resources.require("iam")[0].version
    click.echo(version)

@click.command()
@click.option('--port', type=int, default=5000, help="Port to run the application")
def start_server(port):
    """Starts the web server"""
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine.base.Engine').setLevel(logging.ERROR)

    from waitress import serve
    serve(APP, listen='*:{0}'.format(port), connection_limit=1000, asyncore_use_poll=True)
    
web.add_command(version)
web.add_command(start_server)