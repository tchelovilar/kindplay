import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

install_requires = (here / 'kindplay.egg-info/requires.txt').read_text(encoding='utf-8').splitlines()

setup(
    install_requires=install_requires
)
