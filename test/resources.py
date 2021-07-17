from os.path import join, dirname


def resource(filename: str) -> str:
    with open(join(dirname(__file__), 'resources', filename)) as file:
        return file.read()
