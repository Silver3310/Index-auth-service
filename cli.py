"""A Convenient Command Line Interface for common tasks"""
import click
import sys
from subprocess import call


@click.group()
def cli():
    """Command Line Interface for the PrivetThere project"""
    pass


@click.command()
def runserver():
    """Run the project"""
    call(
        'docker-compose -f local.yml up'.split()
    )


@click.command()
def stop():
    """Stop the project"""
    call(
        'docker-compose -f local.yml stop'.split()
    )


@click.command()
def test():
    """Test the project"""
    call(
        'docker exec -ti index-auth-service_django_1 sh -c'.split()
        + [
            "source compose/production/django/entrypoint && pytest"
        ]
    )


@click.command()
def shp():
    """Open the project's shell_plus"""
    call(
        'docker exec -ti index-auth-service_django_1 sh -c'.split()
        + [
            "source compose/production/django/entrypoint && "
            "python manage.py shell_plus"
        ]
    )


@click.command()
def cov():
    """Test the project with coverage and html report"""
    call(
        'docker exec -ti index-auth-service_django_1 sh -c'.split()
        + [
            "source compose/production/django/entrypoint && "
            "coverage run -m pytest && coverage html"
        ]
    )


@click.command(context_settings=dict(
    allow_extra_args=True,
))
def rc():
    """Run an arbitrary command"""
    command = ' '.join(sys.argv[2:])
    call(
        'docker exec -ti index-auth-service_django_1 sh -c'.split()
        + [f"source compose/production/django/entrypoint && {command}"]
    )


cli.add_command(runserver)
cli.add_command(stop)
cli.add_command(test)
cli.add_command(shp)
cli.add_command(cov)
cli.add_command(rc)


if __name__ == '__main__':
    cli()
