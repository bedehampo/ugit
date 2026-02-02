from setuptools import setup

setup (
    name = 'ugit',
    version = '0.1',
    py_modules = ['cli'],
    entry_points = {
        'console_scripts': ['ugit=cli:main']
    }
)