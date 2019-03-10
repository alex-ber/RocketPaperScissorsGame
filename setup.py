import setuptools
from setuptools import setup
import os

print(__file__)
#print(os.path.realpath(__file__))
requirementPath = os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt'

install_requires = []
with open(requirementPath) as f:
    install_requires = f.read().splitlines()





setup(
    name='rocket-paper-scissors-gmae',
    version='0.0.1',
    url='https://github.com/alex-ber/rockerpaperscissorsgame',
    author='Alexander Berkovich',
    description='Rock-Paper-Scissors game',
    long_description='Engine and some refference implementation of Rock-Paper-Scissors game.',
    packages=setuptools.find_packages(exclude=('tests*',)),
    install_requires=install_requires,
    namespace_packages=('alexber',),
    license='Apache 2.0',
    keywords='game engine player rock papaer scissors',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        "Topic :: Utilities",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Development Status :: 1 - Planning',
        'Environment :: Console'

    ],
    include_package_data=True,
    platforms='Windows'
)