# -*- coding: utf-8 -*-

"""
test_app
----------------------------------
Tests for `projectpyspark2.app` module.
"""
import os
import sys

from unittest.mock import MagicMock
import pytest

from projectpyspark2.app import run

import sparkutils

def test_no_args():
    # GIVEN
    sys.argv = [__file__]

    # WHEN
    ret_code = run()

    # THEN
    assert ret_code == -1

def test_run(monkeypatch):
    """
    Test run method
    """
    # GIVEN
    spark = MagicMock()
    config = MagicMock()
    config.getString = MagicMock(return_value=os.path.realpath(__file__))

    monkeypatch.setattr(sparkutils, 'run', lambda task : task.runProcess(spark, config))

    sys.argv = [__file__, ""]

    # WHEN
    ret_code = run()

    # THEN
    assert ret_code == 0
