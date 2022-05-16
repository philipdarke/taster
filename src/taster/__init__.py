"""Add an introduction to the ``taster`` module in ``__init__.py``.
"""


from importlib.metadata import version

__version__ = version("taster")

from taster.taster import *  # noqa: F401, F403

__all__ = []
for module in dir():
    if not module.startswith("__") and module != "taster":
        __all__.append(module)
