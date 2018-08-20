from setuptools import setup

setup(
    name='mangareaderlib',
    url='https://github.com/tarikyayla/mangareaderlib',
    author='Tarık Yayla',
    author_email='tarik.yayla33@gmail.com',
    packages=['mangareaderlib'],
    install_requires=['beautifulsoup4','tqdm','requests'],
    version='0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.md').read(),
)

