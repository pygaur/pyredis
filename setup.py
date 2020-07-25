"""
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyredis",
    version="1.0",
    author="Prashant Gaur",
    author_email="91prashantgaur@gmail.com",
    description="A python wrapper for easy interaction with redis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pygaur/pyredis",
    packages=setuptools.find_packages(),
    install_requires=[
        "redis",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)