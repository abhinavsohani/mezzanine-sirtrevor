#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='sirtrevor',
    version= '0.2.3',
    packages=['sirtrevor'],
    include_package_data=True,
    license='MIT License',
    description='Sir Trevor editor for Mezzanine',
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/thecodinghouse/mezzanine-sirtrevor',
    author='Abhinav Sohani',
    author_email='hello@thecodinghouse.in',
    install_requires=['markdown2', 'django-appconf', 'django', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
