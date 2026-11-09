import pytest

from predicate import ge_p
from pytest_predicate import assert_matches, assert_not_matches


def test_assert_matches():
    assert_matches(10, ge_p(5))


def test_assert_matches_failure():
    with pytest.raises(AssertionError):
        assert_matches(3, ge_p(5))


def test_assert_not_matches():
    assert_not_matches(3, ge_p(5))


def test_assert_not_matches_failure():
    with pytest.raises(AssertionError, match="but it did"):
        assert_not_matches(10, ge_p(5))