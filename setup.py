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
    package_dir={'djblog': 'djblog'},
    include_package_data=True,
    install_requires=[
        'django>=1.5',
        'django-extensions==1.3.3',
        'mistune==0.1.0',
        'Pygments==1.6'
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
