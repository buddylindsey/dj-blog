=============================
dj-blog
=============================

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

Finally, you need to writey our own templates and put them in djblog/ in your templates folder.
