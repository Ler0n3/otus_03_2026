import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.circle import Circle
from src.square import Square


@pytest.mark.parametrize(
    argnames='side_a, side_b',
    argvalues=[
        pytest.param(0, 5, id='zero first'),
        pytest.param(14, 0, id='zero second'),
        pytest.param(-3.5, 5.5, id='negative numbers first'),
        pytest.param(12.5, -27.1, id='negative numbers second')
    ],
)
def test_invalid_value_sides(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    argnames='side_a, side_b',
    argvalues=[
        pytest.param('abc', 5, id='string first'),
        pytest.param(34.86, 'def', id='string second'),
        pytest.param('abc', 'def', id='two string'),
        pytest.param(None, 5, id='None'),
        pytest.param(5, [1, 2], id='list'),
        pytest.param({'side_a': 54}, 8, id='dict'),
    ]
)
def test_invalid_type_sides(side_a, side_b):
    with pytest.raises(TypeError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    argnames='side_a, side_b, area',
    argvalues=[
        (3, 5, 15),
        (3.5, 5.5, 19.25),
    ]
)
def test_calculate_area_rectangle(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Area of rectangle with sides {side_a} and {side_b} must be {area}, actual is {r.area}'


@pytest.mark.parametrize(
    argnames='side_a, side_b, perimeter',
    argvalues=[
        (8, 5, 26),
        (8.47, 6.28, 29.5),
    ]
)
def test_calculate_perimeter_rectangle(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, (f'Perimeter of rectangle with sides {side_a} and {side_b} must be {perimeter},'
                                      f' actual is {r.perimeter}')


@pytest.mark.parametrize(
    argnames='other_figure, area',
    argvalues=[
        pytest.param(Rectangle(4, 6), 39, id='rectangle with sides 4 and 6'),
        pytest.param(Square(6), 51, id='square with side 6'),
        pytest.param(Triangle(3, 4, 5), 21, id='triangle with sides 3-4-5'),
        pytest.param(Circle(3), 43.27, id='circle with radius 3')
    ]
)
def test_add_area_valid_figure(other_figure, area):
    r = Rectangle(3, 5)
    result = r.add_area(other_figure)
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
    r = Rectangle(4, 6)
    with pytest.raises(ValueError):
        r.add_area(invalid_value)
