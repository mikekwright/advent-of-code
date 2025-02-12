from src.santa_miner import find_the_santa_mine


def test_santa_mine__returns_609043__for_abcdef_for_first_5_zeros():
    expected_value = 609043

    actual_value = find_the_santa_mine('abcdef')

    assert expected_value == actual_value


def test_santa_mine__returns_31556__for_abcdef_for_first_4_zeros():
    expected_value = 31556

    actual_value = find_the_santa_mine('abcdef', count=4)

    assert expected_value == actual_value


def test_santa_mine__returns_72162__for_abcdef_for_first_4_zeros_but_starting_at_over_40000():
    expected_value = 72162

    actual_value = find_the_santa_mine('abcdef', count=4, start_num=40000)

    assert expected_value == actual_value


def test_santa_mine__returns_1048970__for_pqrstuv_for_first_5_zeros():
    expected_value = 1048970

    actual_value = find_the_santa_mine('pqrstuv')

    assert expected_value == actual_value

