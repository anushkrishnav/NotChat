import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from myapi.extensions import db
    from myapi.models import User

    click.echo("create user")
    user = User(username="anushkrishnav", email="anush.venkatakrishna@gmail.com", password="Look1ngf0r@safew0rd", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
