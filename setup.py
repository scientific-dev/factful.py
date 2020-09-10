from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="factful.py",
    version="0.0.7",
    description="A Package which can give you Random Facts in an easy way!",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=['factful'],
    keywords="factful.py",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)
