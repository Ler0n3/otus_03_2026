import pytest
from src.circle import Circle
from src.square import Square
from src.rectangle import Rectangle
from src.triangle import Triangle


@pytest.mark.parametrize(
    argnames='radius',
    argvalues=[
        pytest.param(0, id='zero'),
        pytest.param(-3.5, id='negative numbers'),
    ],
)
def test_invalid_value_sides(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    argnames='radius',
    argvalues=[
        pytest.param('abc', id='string'),
        pytest.param(None, id='None'),
        pytest.param([1, 2], id='list'),
        pytest.param({'side_a': 54}, id='dict'),
    ]
)
def test_invalid_type_sides(radius):
    with pytest.raises(TypeError):
        Circle(radius)


@pytest.mark.parametrize(
    argnames='radius, area',
    argvalues=[
        (3, 28.27),
        (3.5, 38.48),
    ]
)
def test_calculate_area_circle(radius, area):
    c = Circle(radius)
    assert round(c.area, 2) == area, f'Area of circle with radius {radius} must be {area}, actual is {c.area}'


@pytest.mark.parametrize(
    argnames='radius, perimeter',
    argvalues=[
        (8, 50.27),
        (6.3, 39.58),
    ]
)
def test_calculate_perimeter_circle(radius, perimeter):
    c = Circle(radius)
    assert round(c.perimeter, 2) == perimeter, (f'Perimeter of circle with radius {radius} must be {perimeter},'
                                                f' actual is {c.perimeter}')


@pytest.mark.parametrize(
    argnames='other_figure, area',
    argvalues=[
        pytest.param(Rectangle(4, 6), 74.27, id='rectangle with sides 4 and 6'),
        pytest.param(Square(6), 86.27, id='square with side 6'),
        pytest.param(Triangle(3, 4, 5), 56.27, id='triangle with sides 3-4-5'),
        pytest.param(Circle(3), 78.54, id='circle with radius 3')
    ]
)
def test_add_area_valid_figure(other_figure, area):
    c = Circle(4)
    result = c.add_area(other_figure)
    assert round(result, 2) == area


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
    c = Circle(6)
    with pytest.raises(ValueError):
        c.add_area(invalid_value)
