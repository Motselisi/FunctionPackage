from setuptools import setup, find_packages

setup(
    name='FunctionPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Motselisi/FunctionPackage',
    author='Motselisi',
    author_email='motselisileketa@gmail.com'
)
