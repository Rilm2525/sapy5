from setuptools import setup, find_packages

setup(
    name='sapy5',
    version='0.0.0.2',
    license='MIT',
    description='Makes it easy to use sapi from Python.',

    author='Rilm2525',
    author_email='rilm2525ce@gmail.com',
    url='https://twitter.com/Rilm2525',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
