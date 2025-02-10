from src.wrapping import calculate_wrapping, calculate_all_wrapping_feet, calculate_all_ribbon


def test_calculate_wrapping__returns_area_58__for_input_of_2x3x4():
    expected_area = 58

    actual_wrapping = calculate_wrapping('2x3x4')

    assert expected_area == actual_wrapping.total_area


def test_calculate_wrapping__returns_area_43__for_input_of_1x1x10():
    expected_area = 43

    actual_wrapping = calculate_wrapping('1x1x10')

    assert expected_area == actual_wrapping.total_area


def test_calculate_all_wrapping_feet__returns_58__for_one_input_of_2x3x4():
    expected_area = 58

    actual_area = calculate_all_wrapping_feet(['2x3x4'])

    assert expected_area == actual_area


def test_calculate_all_wrapping_feet__returns_101__for_two_inputs():
    expected_area = 101

    actual_area = calculate_all_wrapping_feet(['2x3x4', '1x1x10'])

    assert expected_area == actual_area


def test_calculate_wrapping__returns_ribbon_34__for_input_of_2x3x4():
    expected_ribbon = 34

    actual_wrapping = calculate_wrapping('2x3x4')

    assert expected_ribbon == actual_wrapping.ribbon


def test_calculate_wrapping__returns_ribbon_14__for_input_of_1x1x10():
    expected_ribbon = 14

    actual_wrapping = calculate_wrapping('1x1x10')

    assert expected_ribbon == actual_wrapping.ribbon


def test_calculate_all_ribbon__returns_48__for_two_inputs():
    expected_ribbon = 48

    actual_ribbon = calculate_all_ribbon(['2x3x4', '1x1x10'])

    assert expected_ribbon == actual_ribbon

