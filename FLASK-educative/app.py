import click
from flask import Flask

app = Flask(__name__)

@app.cli.command("create_user")
@click.argument("name")
def create_user(name):
    print('Created user, ' + name)


# flask create_user <your name>


# https://www.youtube.com/watch?v=wyG3BiL-E5c&ab_channel=PrettyPrinted