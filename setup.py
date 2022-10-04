import os
import pyximport
pyximport.install(pyimport=True)
import pkg_resources
from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize;
from Cython.Compiler import Options
Options.infer_types = True
Options.language_level = 3
extensions = [Extension('*',['/jukebox/*.py'])];

setup(
    name="jukebox",
    py_modules=["jukebox"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    ext_modules=cythonize(extensions),
    include_package_data=True
)
