import re
from setuptools import setup

with open("cricinfo/__init__.py") as file:
    version = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE
    ).group(1)

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as readme:
    readme = readme.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent",
    "Topic :: Internet",
    "Topic :: Utilities",
]

setup(
    name = "pycricinfo",
    author = "Farhan Ahmed",
    url="https://github.com/UnrealFar/cricinfoapi",
    version=version,
    description="A useful Python wrapper to scrape the ESPN Cricinfo JSON API.",
    long_description=readme,
    license="MIT",
    install_requires=requirements,
    extras_require={"docs": ["sphinx", "furo"]},
    packages=("cricinfo",),
    include_package_data=True,
    classifiers=classifiers,
    python_requires=">=3.10",
    keywords=["cricinfo", "espncricinfo", "pycricinfo", "espn", "cricket", "api", "wrapper", "scraper"],
)
