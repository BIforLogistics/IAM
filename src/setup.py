from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="IAM",
    version="0.0.1",
    description="Identity Access Management",
    entry_points='''
    [console_scripts]
    iam=iam:web
    ''',
    py_modules=['src'],
    scripts=['iam.py']
)