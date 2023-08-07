from setuptools import setup, find_packages

setup(
    name='owologger',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "discord.py>=1.7.3",
        "discord>=1.7.3",
        "colorama",
        "logging",
    ],
)
