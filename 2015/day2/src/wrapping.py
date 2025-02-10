from dataclasses import dataclass

@dataclass
class Wrapping:
    total_area: float
    smallest_area: float
    ribbon: float


def calculate_wrapping(single_entry: str) -> Wrapping:
    dimensions = [int(d) for d in single_entry.split('x')]

    areas = (
        (dimensions[0] * dimensions[1]),
        (dimensions[1] * dimensions[2]),
        (dimensions[2] * dimensions[0])
    )

    smallest_area = min(areas)
    total_area = sum(d * 2 for d in areas) + smallest_area

    perimeters = (
        (dimensions[0] * 2 + dimensions[1] * 2),
        (dimensions[1] * 2 + dimensions[2] * 2),
        (dimensions[2] * 2 + dimensions[0] * 2)
    )

    cubic = (dimensions[0] * dimensions[1] * dimensions[2])
    ribbon = min(perimeters) + cubic
    return Wrapping(total_area, smallest_area, ribbon)


def calculate_all_wrapping_feet(entries: list[str]) -> float:
    return sum(calculate_wrapping(e).total_area for e in entries)

def calculate_all_ribbon(entries: list[str]) -> float:
    return sum(calculate_wrapping(e).ribbon for e in entries)
