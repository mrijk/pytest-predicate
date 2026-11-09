from predicate import ge_p, le_p


def test_integer_predicate(predicate_examples):
    predicate = ge_p(10) & le_p(20)

    matching = predicate_examples.matching(predicate, count=10)
    non_matching = predicate_examples.non_matching(predicate, count=10)

    assert all(predicate(x) for x in matching)
    assert all(not predicate(x) for x in non_matching)