#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="zodbbrowser",
    maintainer="Programmers of Vilnius",
    maintainer_email="tautvilas@pov.lt",
    description="ZODB browser",
    version="0.2",
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    install_requires=[
        "ZODB3",
        "zope.app.pagetemplate",
        "zope.app.publication",
        "zope.component",
        "zope.interface",
        "zope.location",
        "zope.publisher",
        "zope.security",
        "zope.traversing",
        "simplejson",
        ],
    extras_require=dict(
        test=["zope.app.container",
              "zope.testbrowser",
              "zope.app.testing",
             ],
    ),
)
