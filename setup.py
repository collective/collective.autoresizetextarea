from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='collective.autoresizetextarea',
      version=version,
      description="jQuery textarea auto-resizer for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='jQuery textarea auto-resize',
      author='Timo Stollenwerk',
      author_email='timo@zmag.de',
      url='http://pypi.python.org/pypi/collective.autoresizetextarea',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      paster_plugins = ["ZopeSkel"],
      )
