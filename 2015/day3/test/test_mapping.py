from src.mapping import SantaGrid, SantaTracker


def test_santa_grid__returns_unique_visits__when_multiple_visits_added():
    expected_visits = 2

    test_model = SantaGrid()

    test_model.add_visit(0, 0)
    test_model.add_visit(1, 1)
    test_model.add_visit(0, 0)

    actual_visits = test_model.unique_visits()

    assert expected_visits == actual_visits


def test_santa_tracker__has_one_present__when_first_created():
    expected_presents = 1

    test_model = SantaTracker()

    actual_presents = test_model.presents_delivered()

    assert expected_presents == actual_presents


def test_santa_tracker__has_2_present__when_one_direction_given():
    expected_presents = 2

    test_model = SantaTracker()
    test_model.move('>')

    actual_presents = test_model.presents_delivered()

    assert expected_presents == actual_presents


def test_santa_tracker__has_4_presents__when_directions_dont_overlap():
    expected_presents = 4

    test_model = SantaTracker()
    for direction in '^>v<':
        test_model.move(direction)

    actual_presents = test_model.presents_delivered()

    assert expected_presents == actual_presents
