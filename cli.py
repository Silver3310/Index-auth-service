"""A Convenient Command Line Interface for common tasks"""

import sys
from subprocess import call


def run_command(arg):
    # run an arbitrary command
    call(
        'docker exec -ti index-auth-service_django_1 sh -c'.split()
        + [f"source compose/production/django/entrypoint && {arg}"]
    )


if __name__ == "__main__":
    command = ' '.join(sys.argv[1:])

    run_command(command)


