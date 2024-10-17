import functions as soln


def test_check_duplicate_value_case_0():
    assert soln.max_length({"four score", "and", "seven", "years ago our forefathers"}) == 24