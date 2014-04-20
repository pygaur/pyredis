from setuptools import setup, find_packages

setup(name="pyredis",
      version="1.0",
      author="Prashant Gaur",
      author_email = "91prashantgaur@gmail.com",
      description = "An open source api to handle redis method in python .Needed redis as python redis connetor.",
      url = "gaurprashant.blogspot.in",
      packages=find_packages(),
      install_requires=[
            "redis==2.9.1",
        ],
      include_package_data=True,
      )
