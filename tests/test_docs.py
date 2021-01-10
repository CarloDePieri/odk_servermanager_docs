import pytest
from invoke import Context
from os.path import exists, join, isdir
from os import mkdir, getcwd, chdir
from shutil import rmtree
from unittest.mock import patch


import sys
sys.path.append('.')
# This import MUST be AFTER the sys path append!
import tasks  # nopep8


_BUILD_FOLDER = join("tests", "build")
_HTML_BUILD_FOLDER = join(_BUILD_FOLDER, "html")
_HTML_IT_BUILD_FOLDER = join(_HTML_BUILD_FOLDER, "it")
_GETTEXT_BUILD_FOLDER = join(_BUILD_FOLDER, "gettext")
_SOURCE_FOLDER = join('tests', 'source')  # don't patch this in the whole class


@patch("tasks.BUILD_FOLDER", _BUILD_FOLDER)
@patch("tasks.HTML_BUILD_FOLDER", _HTML_BUILD_FOLDER)
@patch("tasks.HTML_IT_BUILD_FOLDER", _HTML_IT_BUILD_FOLDER)
@patch("tasks.GETTEXT_BUILD_FOLDER", _GETTEXT_BUILD_FOLDER)
class TestODKSMDocs:
    """Test: ODKSMDocs..."""

    def _clean(self):
        if (isdir(_BUILD_FOLDER)):
            rmtree(_BUILD_FOLDER)
        if (isdir(_SOURCE_FOLDER)):
            rmtree(_SOURCE_FOLDER)

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        """TestAConfigIni setup"""
        # Make sure to start fresh
        self._clean()
        yield

    @pytest.fixture(scope="function", autouse=True)
    def single_test_cleanup(self):
        yield
        # Cleanup after each test. Comment this out to inspect test artifacts
        self._clean()

    def test_should_build_eng_html(self):
        """It should build eng html"""
        c = Context()
        tasks.build_html(c)
        assert exists(join(tasks.HTML_BUILD_FOLDER, "index.html"))

    def test_should_build_gettext_artifacts(self):
        """It should build gettext artifacts"""
        c = Context()
        tasks.build_gettext(c)
        assert exists(join(tasks.GETTEXT_BUILD_FOLDER, "index.pot"))

    def test_should_build_locales_files(self):
        """It should build locales files"""
        c = Context()
        tasks.build_gettext(c)
        if not isdir(_SOURCE_FOLDER):
            mkdir(_SOURCE_FOLDER)
        with patch('tasks.SOURCE_FOLDER', _SOURCE_FOLDER):
            cwd = getcwd()
            tasks.build_it_docs(c)
            chdir(cwd)
            assert exists(join(_SOURCE_FOLDER, 'locales', 'it', 'LC_MESSAGES', 'index.po'))

    def test_should_build_italian_html(self):
        """It should build italian html"""
        c = Context()
        tasks.build_it_html(c)
        assert exists(join(tasks.HTML_IT_BUILD_FOLDER, "index.html"))
