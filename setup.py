from setuptools import setup, find_packages
import subprocess
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="iliantest",
    version="0.0.1",
    author="ILian",
    author_email="ilian@iazz.fr",
    description="azdadz",
    long_description=long_description,
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