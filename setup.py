# -*- coding: utf-8 -*-

from setuptools import setup

project = "futbol"

setup(
    name=project,
    version='0.1',
    url='https://github.com/rberezin/desarrolloWeb',
    description='',
    author='',
    author_email='',
    packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
