from predicate.predicate import Predicate


def assert_matches[T](value: T, predicate: Predicate[T]) -> None:
    if predicate(value):
        return

    explanation = predicate.explain_failure(value)

    raise AssertionError(
        f"Value {value!r} does not match {predicate!r}.\n"
        f"Explanation: {explanation}"
    )


def assert_not_matches[T](value: T, predicate: Predicate[T]) -> None:
    if not predicate(value):
        return

    raise AssertionError(
        f"Expected {value!r} not to match {predicate!r}, "
        f"but it did."
    )