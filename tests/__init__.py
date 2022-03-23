import importlib.machinery
import importlib.util
import io
import pkgutil
from types import FunctionType, ModuleType
from unittest import mock


def import_module(name: str, source_path: str) -> ModuleType:
    """Import and return a module from the file system.

    :param name: the name of the module.
    :param source_path: the file system path where the module is located.

    Used when the module is written in a file without the `.py`
    extensions (for example, `cli/rfrb` or `bin/rfrb`).

    Thanks to [anthonywritescode](https://www.youtube.com/watch?v=B5bToFdBxdw)
    for explaining so well how to do it.

    :return: the module loaded from the file system.
    """
    # creates a source code loader and load the module spec
    loader = importlib.machinery.SourceFileLoader(name, source_path)
    spec = importlib.util.spec_from_loader(loader.name, loader)

    # turns the spec into a module, and "make it alive"
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)

    return mod


class ResponseBuilder(object):
    """
    Build a function that mocks a response from the `requests` library.

    Used to patch unit tests.
    """

    def __init__(self, filename, status_code=200):
        self.filename = filename
        self.status_code = status_code

    def __call__(self, _) -> FunctionType:
        return self._build_response()

    def _build_response(self) -> FunctionType:
        """
        Build a response object with a subset of the response object
        from the requests API.
        """
        resource = pkgutil.get_data("tests", self.filename)
        text = io.BytesIO(resource).read().decode("UTF-8")

        mock_response = mock.Mock()
        mock_response.text = text
        mock_response.ok = self.status_code == 200
        mock_response.status_code = self.status_code

        return mock_response
