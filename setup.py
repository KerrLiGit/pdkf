from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='pdkf',
  version='1.0.4',
  author='KerrLi',
  author_email='bogatyreva_aa@mail.ru',
  description='Module for working with PDKF files and Pandas dataframes',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/KerrLiGit/pdkf',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='pdkf',
  project_urls={
    'Documentation': 'https://github.com/KerrLiGit/pdkf/wiki'
  },
  install_requires=[
    'pandas>=2.1.0',
    'zipp>=3.17.0'
  ],
  python_requires='>=3.7'
)