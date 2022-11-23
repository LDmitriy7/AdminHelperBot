import warnings
from pathlib import Path

from envparse import Env as RawEnv, NOTSET


class Env:

    def __init__(self, path: str):
        self._path = Path(path)
        self._raw = RawEnv()
        self._read_file()

    def _read_file(self):
        path = self._path

        if not path.exists():
            warnings.warn(f'File {path} not found')

        self._raw.read_envfile(path)

    def get(self, var_name: str, default=...) -> str:
        if default is ...:
            default = NOTSET

        return self._raw(var_name, default)

    def get_int(self, var_name: str, default=...) -> int:
        return int(self.get(var_name, default))


env = Env('.env')
