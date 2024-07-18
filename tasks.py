import os

from invoke import task
from os.path import join

SOURCE_FOLDER = join("docs", "source")
BUILD_FOLDER = join("docs", "build")
HTML_BUILD_FOLDER = join(BUILD_FOLDER, "html")
HTML_IT_BUILD_FOLDER = join(HTML_BUILD_FOLDER, "it")
GETTEXT_BUILD_FOLDER = join(BUILD_FOLDER, "gettext")
POETRY_RUN = "poetry run"
INTL_BIN = f"{POETRY_RUN} sphinx-intl"
BUILD_BIN = f"{POETRY_RUN} sphinx-build"

# Disable the pipenv spam about already being inside a venv
os.environ["PIPENV_VERBOSITY"] = "-1"


@task
def clean(c):
    print("\n>> Cleaning all built documentation.\n")
    c.run(f"{POETRY_RUN} {join('docs', 'make')} clean")


@task
def clean_html(c):
    print("\n>> Cleaning html documentation.\n")
    c.run(f"rm -rf {HTML_BUILD_FOLDER}")


@task
def build_gettext(c):
    print("\n>> Building gettext...\n")
    c.run(f"{BUILD_BIN} -b gettext {SOURCE_FOLDER} {GETTEXT_BUILD_FOLDER}")


@task(build_gettext)
def build_it_docs(c):
    print("\n>> Building italian translation files...\n")
    os.chdir(SOURCE_FOLDER)
    c.run(f"{INTL_BIN} update -p {join('..', 'build', 'gettext')} -l it")


@task()
def build_it_html(c):
    print("\n>> Building italian html docs...\n")
    c.run(f"{BUILD_BIN} -b html -D language=it {SOURCE_FOLDER} {HTML_IT_BUILD_FOLDER}")


@task()
def build_html(c):
    print("\n>> Building english html docs...\n")
    c.run(f"{BUILD_BIN} -b html -D language=en {SOURCE_FOLDER} {HTML_BUILD_FOLDER}")


@task(build_it_html, build_html)
def build(c):
    """A task to build both the english and italian documentation."""
    pass


@task()
def serve(c):
    # noinspection PyPackageRequirements
    from livereload import Server
    server = Server()
    # Build the docs for the first time
    build_html(c)
    print("\n>> Docs built! Serving and watching for changes...\n")
    # Watch for changes in rst files; rebuild the html documentation when it happens
    server.watch('docs/source/*.rst', lambda: build_html(c))
    # Serve the built docs. This will autoreload on change!
    server.serve(root='docs/build/html', port=5500)


@task()
def serve_it(c):
    from livereload import Server
    server = Server()

    def _build_it_docs(c):
        build_gettext(c)
        cwd = os.getcwd()
        build_it_docs(c)
        os.chdir(cwd)

    # Build the docs for the first time
    _build_it_docs(c)
    build_it_html(c)
    print("\n>> Docs built! Serving and watching for changes...\n")

    # Watch for any changes in rst files: rebuild po files when it happens
    server.watch('docs/source/*.rst', lambda: _build_it_docs(c))
    # Watch for any changes in po files; rebuild the html documentation when it happens
    server.watch("docs/source/locales/it/LC_MESSAGES/*.po", lambda: build_it_html(c))
    # Serve the built docs. This will autoreload on change!
    server.serve(root='docs/build/html/it', port=5501)


@task()
def test(c):
    print("\n>> Testing the whole pipeline...\n")
    c.run(f"{POETRY_RUN} pytest -s tests")
