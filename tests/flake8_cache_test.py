from __future__ import annotations

import ast

from flake8_pyspark_cache import Plugin


def results(s):
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


def test_trivial():
    assert not results("")


def test_assignment_expression_not_ok():
    src = """\
df.cache()
"""
    (msg,) = results(src)
    assert msg == "1:0: PS002 do not use cache()"
