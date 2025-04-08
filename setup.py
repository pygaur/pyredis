"""
Python package setup for pyredis
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart-redis-cache",  # Changed name to avoid conflict with existing PyPI packages
    version="1.0.0",
    author="Prashant Gaur",
    author_email="91prashantgaur@gmail.com",
    description="A Pythonic wrapper for easy interaction with Redis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pygaur/pyredis",
    project_urls={
        "Bug Tracker": "https://github.com/pygaur/pyredis/issues",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        "redis",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="redis, cache, database, dictionary, hash, list, set",
    python_requires='>=3.6',
)