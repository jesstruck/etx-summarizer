import setuptools
from etx import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etx-sum", # Replace with your own username
    version=__version__,
    author="Jes Struck",
    author_email="mail@jesstruck.dk",
    description="ext-sum.py is intended to be a small utillity script that gives a few greate stats on your daytrading results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jesstruck/etx-summarizer",
    packages=setuptools.find_packages(),
    entry_points = {
      'console_scripts': [
        'etx-sum = etx.__main__:main'
      ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
