import sys

from django.conf import settings

settings.configure(
    TIME_ZONE='UTC',
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    },
    ROOT_URLCONF="djblog.urls",
    INSTALLED_APPS=[
        "django.contrib.sites",
        "djblog",
    ],
    SITE_ID=1,
)

from django_nose import NoseTestSuiteRunner

test_runner = NoseTestSuiteRunner(verbosity=2)
failures = test_runner.run_tests(["."])

if failures:
    sys.exit(failures)
