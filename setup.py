import os
from setuptools import setup, find_packages

setup(name='testapp',
      version = '0.1dev',
      description="A minimal Cromlech setup.",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'cromlech.webob',
                        'cromlech.io',
                        'cromlech.dawnlight',
                        'cromlech.browser',
                        'cromlech.configuration',
                        'dolmen.view'
                        ],
      entry_points="""
      [fanstatic.libraries]
      testapp = testapp.resources:testapp_library

      [paste.app_factory]
      testapp = testapp.main:testapp
      """,
      )
