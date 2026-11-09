from collections.abc import Callable
from dataclasses import dataclass
from itertools import islice
from typing import Any

import pytest
from predicate import generate_false, generate_true
from predicate.predicate import Predicate


@dataclass
class PredicateExamples:
    def matching[T](
        self,
        predicate: Predicate[T],
        *,
        count: int = 10,
    ) -> list[T]:
        return list(islice(generate_true(predicate), count))

    def non_matching[T](
        self,
        predicate: Predicate[T],
        *,
        count: int = 10,
    ) -> list[T]:
        return list(islice(generate_false(predicate), count))


@pytest.fixture
def predicate_examples() -> PredicateExamples:
    return PredicateExamples()