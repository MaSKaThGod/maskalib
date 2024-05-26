from setuptools import setup, find_packages

setup(
    name='maskalib',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'datetime'
    ],
    author='maska',
    author_email='maska@maska.ai',
    description='A Python library for MaskaAI interactions.',
    url='https://github.com/MaSKaThGod/',
)