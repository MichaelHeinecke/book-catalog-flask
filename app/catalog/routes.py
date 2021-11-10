from app.catalog import main


@main.route('/')
def hello():
    return 'Hello world!'
