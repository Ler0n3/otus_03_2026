import pytest
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.circle import Circle
from src.square import Square


@pytest.mark.parametrize(
    argnames='side_a, side_b, side_c',
    argvalues=[
        pytest.param(0, 5, 8, id='zero first'),
        pytest.param(3, 0, 8, id='zero second'),
        pytest.param(3, 5, 0, id='zero third'),
        pytest.param(-3.5, 5.5, 12.4, id='negative numbers first'),
        pytest.param(3.5, -5.5, 12.4, id='negative numbers second'),
        pytest.param(3.5, 5.5, -12.4, id='negative numbers third')
    ],
)
def test_invalid_value_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    argnames='side_a, side_b, side_c',
    argvalues=[
        pytest.param('abc', 5, 9, id='string first'),
        pytest.param(34.86, 'def', 74.2, id='string second'),
        pytest.param(12, 20, 'ghi', id='string third'),
        pytest.param('abc', 'def', 'ghi', id=' three string'),
        pytest.param(2, None, 5, id='None'),
        pytest.param(25, 5, [1, 2], id='list'),
        pytest.param({'side_a': 54}, 8, 9, id='dict'),
    ]
)
def test_invalid_type_sides(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    argnames='side_a, side_b, side_c',
    argvalues=[
        pytest.param(1, 1, 3, id='1+1 < 3'),
        pytest.param(10, 3, 1, id='1+3 < 10'),
        pytest.param(1, 10, 5, id='1+5 < 10'),
        pytest.param(1, 2, 3, id='1+2 = 3'),
        pytest.param(4, 2, 2, id='2+2 = 4'),
        pytest.param(3, 7, 4, id='3+4 = 7'),
        pytest.param(1.5, 2.5, 5.0, id='1.5+2.5 < 5.0'),
        pytest.param(5.0, 2.5, 2.5, id='2.5+2.5 = 5.0'),
    ]
)
def test_triangle_inequality_error(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    argnames='side_a, side_b, side_c, area',
    argvalues=[
        (3, 4, 5, 6),
        (5, 5, 6, 12),
        (5, 5, 5, 10.83),
        (2.5, 3.5, 4.5, 4.35)
    ]
)
def test_calculate_area_triangle(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert round(t.area, 2) == area, (f'Area of triangle with sides {side_a}, {side_b} and {side_c} must be {area}, '
                                      f'actual is {t.area}')


@pytest.mark.parametrize(
    argnames='side_a, side_b, side_c, perimeter',
    argvalues=[
        (3, 4, 5, 12),
        (5, 5, 6, 16),
        (5, 5, 5, 15),
        (2.5, 3.5, 4.5, 10.5)
    ]
)
def test_calculate_perimeter_triangle(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, (f'Perimeter of triangle with sides {side_a}, {side_b} and {side_c} '
                                      f'must be {perimeter}, actual is {t.perimeter}')


@pytest.mark.parametrize(
    argnames='other_figure, area',
    argvalues=[
        pytest.param(Rectangle(4, 6), 30, id='rectangle with sides 4 and 6'),
        pytest.param(Square(5), 31, id='square with side 5'),
        pytest.param(Triangle(6, 8, 10), 30, id='triangle with sides 6-8-10'),
        pytest.param(Circle(3), 34.27, id='circle with radius 3')
    ]
)
def test_add_area_valid_figure(other_figure, area):
    t = Triangle(3, 4, 5)
    result = t.add_area(other_figure)
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
    t = Triangle(4, 6, 8)
    with pytest.raises(ValueError):
        t.add_area(invalid_value)
