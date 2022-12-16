import pytest

import dz.dz_08122022_zoo as zoo

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (zoo.lion, True),
        (zoo.pinguin1, True),
        (zoo.pinguin2, True),
        (zoo.pinguin3, True),
        (zoo.begemoth, False),
        (zoo.giraffe, True),
        (zoo.zebra, True),
    ],
)

def test_add_animal(n, expected):

    assert zoo.cage1.add_animal(n) == expected
    assert zoo.cage2.add_animal(n) == expected
