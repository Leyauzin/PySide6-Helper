from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "ui/ui_tools.py",
        "ui/ui_inspector.py",
    ], compiler_directives={"language_level": "3"})
)