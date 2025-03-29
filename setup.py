from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

long_description = long_description.replace("![exampleplot.png](exampleplot.png)", "![exampleplot.png](https://raw.githubusercontent.com/HangoverHGV/python-binary-tree/master/exampleplot.png)")


setup(
    name="python-binary-tree",
    version="1.0.0",
    author="HangoverHGV",
    description="Binary tree implementation for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['networkx', 'matplotlib'],
)

