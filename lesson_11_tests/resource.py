from pathlib import Path


def path(file_name):
    base_path = Path(__file__).resolve().parent.parent / 'tests'
    return str(base_path / 'resources' / file_name)