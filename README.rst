=============================
dj-blog
=============================

.. image:: https://travis-ci.org/buddylindsey/dj-blog.png?branch=master
        :target: https://travis-ci.org/buddylindsey/dj-blog

.. image:: https://pypip.in/d/dj-blog/badge.png
        :target: https://pypi.python.org/pypi/dj-blog/0.1.0

Minimal blog that gets you started.

Documentation
-------------

To be added.

Features
--------

* Add blog post
* Categorize posts
* Use Markdown

Constraints
-----------

1. This is not a full featured blog app its enough to get you started
2. This does not mean to be everything in one to compete with wordpress, zinnia or mezzanine
3. You will need to write your own templates, for now.

Quickstart
----------

Install dj-blog

.. code-block:: bash

    pip install dj-blog

Add ``djblog`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS +=(
        "djblog",
    )

Add to the urls.py:

.. code-block:: python

    url(r'^blog/', include('djblog.urls', namespace="djblog")),

Finally, you need to write your own templates and put them in djblog/ in your templates folder.


Changelog
---------

v 0.3
1. Added switch to use jinja templates if django_jinja is installed
2. Fix bug in showing only published articles in category views

v 0.2.5
1. Changed to ``mistune`` markdown converter
2. Added ``primary_category`` method to article
3. Added start to a preview ability of articles
