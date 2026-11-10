
import os
import sys

import pytest

# Add src directory to path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from calculations import area_of_circle, get_nth_fibonacci


def test_area_of_circle():
    """Test area of circle with a positive radius."""
    radius = 5
    expected_area = 78.53981633974483
    assert area_of_circle(radius) == pytest.approx(expected_area)


def test_area_of_circle_zero_radius():
    """Test area of circle with zero radius."""
    radius = 0
    expected_area = 0
    assert area_of_circle(radius) == expected_area


def test_area_of_circle_negative_radius():
    """Test with a negative radius to raise ValueError."""
    radius = -1
    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_area_of_circle_larger_radius():
    """Test area of circle with a larger radius."""
    radius = 10
    expected_area = 314.1592653589793
    assert area_of_circle(radius) == pytest.approx(expected_area)


def test_get_nth_fibonacci_zero():
    """Test Fibonacci sequence at index 0."""
    n = 0
    expected_value = 0
    assert get_nth_fibonacci(n) == expected_value


def test_get_nth_fibonacci_one():
    """Test Fibonacci sequence at index 1."""
    n = 1
    expected_value = 1
    assert get_nth_fibonacci(n) == expected_value


def test_get_nth_fibonacci_ten():
    """Test Fibonacci sequence at index 10."""
    n = 10
    expected_value = 55
    assert get_nth_fibonacci(n) == expected_value


def test_get_nth_fibonacci_negative():
    """Test with a negative number to raise ValueError."""
    n = -1
    with pytest.raises(ValueError):
        get_nth_fibonacci(n)


def test_get_nth_fibonacci_fifteen():
    """Test Fibonacci sequence at index 15."""
    n = 15
    expected_value = 610
    assert get_nth_fibonacci(n) == expected_value


@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (1, 3.141592653589793),
        (2, 12.566370614359172),
        (3, 28.274333882308138),
        (4, 50.26548245743669),
    ],
)
def test_area_of_circle_multiple_values(radius, expected_area):
    """Test area of circle with multiple radius values."""
    assert area_of_circle(radius) == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "n, expected_value",
    [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
    ],
)
def test_get_nth_fibonacci_multiple_values(n, expected_value):
    """Test Fibonacci sequence with multiple values."""
    assert get_nth_fibonacci(n) == expected_value
