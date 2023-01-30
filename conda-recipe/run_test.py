import pyearth
import pytest
import os

pyearth_dir = os.path.dirname(
    os.path.abspath(pyearth.__file__))
os.chdir(pyearth_dir)
pytest.run(module=pyearth)
