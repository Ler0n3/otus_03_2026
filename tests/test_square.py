import pytest
from src.square import Square
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.circle import Circle


@pytest.mark.parametrize(
    argnames='side_a',
    argvalues=[
        pytest.param(0, id='zero'),
        pytest.param(-3.5, id='negative numbers'),
    ],
)
def test_invalid_value_sides(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize(
    argnames='side_a',
    argvalues=[
        pytest.param('abc', id='string'),
        pytest.param(None, id='None'),
        pytest.param([1, 2], id='list'),
        pytest.param({'side_a': 54}, id='dict'),
    ]
)
def test_invalid_type_sides(side_a):
    with pytest.raises(TypeError):
        Square(side_a)


@pytest.mark.parametrize(
    argnames='side_a, area',
    argvalues=[
        (3, 9),
        (3.5, 12.25),
    ]
)
def test_calculate_area_square(side_a, area):
    s = Square(side_a)
    assert s.area == area, f'Area of square with side {side_a} must be {area}, actual is {s.area}'


@pytest.mark.parametrize(
    argnames='side_a, perimeter',
    argvalues=[
        (8, 32),
        (6.3, 25.2),
    ]
)
def test_calculate_perimeter_square(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, (f'Perimeter of square with side {side_a} must be {perimeter},'
                                      f' actual is {s.perimeter}')


@pytest.mark.parametrize(
    argnames='other_figure, area',
    argvalues=[
        pytest.param(Rectangle(4, 6), 40, id='rectangle with sides 4 and 6'),
        pytest.param(Square(6), 52, id='square with side 6'),
        pytest.param(Triangle(3, 4, 5), 22, id='triangle with sides 3-4-5'),
        pytest.param(Circle(3), 44.27, id='circle with radius 3')
    ]
)
def test_add_area_valid_figure(other_figure, area):
    s = Square(4)
    result = s.add_area(other_figure)
    if isinstance(other_figure, Circle):
        assert round(result, 2) == area
    else:
        assert result == area


@pytest.mark.parametrize(
    argnames='invalid_value',
    argvalues=[
        pytest.param('string', id='string'),
        pytest.param(500, id='number'),
        pytest.param(None, id='None'),
        pytest.param([1, 2], id='list'),
        pytest.param({'figure': 5}, id='dict'),
    ]
)
def test_add_area_invalid_value(invalid_value):
    s = Square(6)
    with pytest.raises(ValueError):
        s.add_area(invalid_value)
