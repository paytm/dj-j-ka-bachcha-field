import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

VERSION = __import__("jkbachcha").__version__

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django :: 1.8',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Framework :: Django :: 1.8',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='dj-jkabachcha',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Package to create Json WYSIWYG field for Django models',
    long_description=README,
    url='https://github.com/paytm/dj-j-ka-bachcha-field',
    author='Shrey Agarwal, Taranjeet Singh',
    author_email='shrey.agarwal@paytm.com, reachtotj@gmail.com',
    classifiers=CLASSIFIERS,
)