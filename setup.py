try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

PACKAGE = "djblog"
NAME = "dj-blog"
DESCRIPTION = "a very basic blog app for a django project"
AUTHOR = "Buddy Lindsey, Jr."
AUTHOR_EMAIL = "buddy@buddylindsey.com"
URL = "https://github.com/buddylindsey/dj-blog"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[
        'djblog',
    ],
    install_requires=[
        'django>=1.5',
        'django-extensions==1.3.3',
        'markdown2==2.2.0'
    ],
    zip_safe=False,
    keywords='django blog',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
