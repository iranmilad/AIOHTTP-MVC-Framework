import pathlib
import toml

BASE_DIR = pathlib.Path(__file__).parent.parent
PACKAGE_NAME = 'broker'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf
