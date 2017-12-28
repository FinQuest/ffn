from . import core
from . import data

from .data import get
from .core import *

core.extend_pandas()

__version__ = (0, 3, 3)
