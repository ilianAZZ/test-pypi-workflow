from setuptools import setup, find_packages
import subprocess
import re
import os

def read_long_description():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()

def read_version():
    with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version_file:
        return version_file.read().strip()

setup(
    name="iliantest",
    version=read_version(),
    author="ILian",
    author_email="ilian@iazz.fr",
    description="azdadz",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/ilianAZZ/best-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.26.4',
        'mne>=1.6.1'
    ],
    extras_require={
        'matlab': []
    }
)