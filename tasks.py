import os

from invoke import task
from os.path import join

SOURCE_FOLDER = join("docs", "source")
BUILD_FOLDER = join("docs", "build")
HTML_BUILD_FOLDER = join(BUILD_FOLDER, "html")
HTML_IT_BUILD_FOLDER = join(HTML_BUILD_FOLDER, "it")
GETTEXT_BUILD_FOLDER = join(BUILD_FOLDER, "gettext")
PIPENV = "pipenv run"
INTL_BIN = "{} sphinx-intl".format(PIPENV)
BUILD_BIN = "{} sphinx-build".format(PIPENV)


@task
def clean(c):
    print("\n>> Cleaning all built documentation.\n")
    c.run("{} {} clean".format(PIPENV, join("docs", "make")))


@task
def clean_html(c):
    print("\n>> Cleaning html documentation.\n")
    c.run("rm -rf {}".format(HTML_BUILD_FOLDER))


@task
def build_gettext(c):
    print("\n>> Building gettext...\n")
    c.run("{} -b gettext {} {}".format(BUILD_BIN, SOURCE_FOLDER, GETTEXT_BUILD_FOLDER))


@task(build_gettext)
def build_it_docs(c):
    print("\n>> Building italian translation files...\n")
    os.chdir(SOURCE_FOLDER)
    c.run("{} update -p {} -l it".format(INTL_BIN, join("..", "build", "gettext")))


@task()
def build_it_html(c):
    print("\n>> Building italian html docs...\n")
    c.run("{} -b html -D language=it {} {}".format(BUILD_BIN, SOURCE_FOLDER, HTML_IT_BUILD_FOLDER))


@task()
def build_html(c):
    print("\n>> Building english html docs...\n")
    c.run("{} -b html -D language=en {} {}".format(BUILD_BIN, SOURCE_FOLDER, HTML_BUILD_FOLDER))
