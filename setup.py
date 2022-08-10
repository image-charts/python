# coding=utf-8

from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='image-charts',
  version="6.1.17",
  py_modules=['ImageCharts'],
  url='https://github.com/image-charts/python',
  license='MIT',
  author='Francois-Guillaume Ribreau',
  author_email='github@fgribreau.com',
  description='Official Image-Charts.com API client library',
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires=["requests>=2.24"],
  python_requires='>=3.6',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Communications :: Email',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Software Development :: Libraries',
    'Topic :: Communications :: Chat',
    'Topic :: Utilities'
  ],
)
