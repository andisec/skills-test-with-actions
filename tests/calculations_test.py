
# ==========================================
# System Modules
# ==========================================
import sys
import os

# ==========================================
# Installed Modules
# ==========================================
import pytest

# ==========================================
# Project Modules
# ==========================================
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


# ==========================================
# TEST AREA OF CIRCLE
# ==========================================

def test_area_of_circle_positive_radius():
    """Test area calculation with a positive radius."""
    radius = 1
    result = area_of_circle(radius)

    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test area calculation with zero radius."""
    radius = 0
    result = area_of_circle(radius)

    assert result == 0


def test_area_of_circle_negative_radius():
    """Test that a negative radius raises ValueError."""
    radius = -1

    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_area_of_circle_larger_radius():
    """Test area calculation with a larger radius."""
    radius = 2
    result = area_of_circle(radius)

    assert abs(result - 12.56637) < 1e-5


# ==========================================
# TEST FIBONACCI
# ==========================================

def test_get_nth_fibonacci_zero():
    """Test Fibonacci sequence with n=0."""
    n = 0
    result = get_nth_fibonacci(n)

    assert result == 0


def test_get_nth_fibonacci_one():
    """Test Fibonacci sequence with n=1."""
    n = 1
    result = get_nth_fibonacci(n)

    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test Fibonacci sequence with n=10."""
    n = 10
    result = get_nth_fibonacci(n)

    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test that a negative number raises ValueError."""
    n = -1

    with pytest.raises(ValueError):
        get_nth_fibonacci(n)


def test_get_nth_fibonacci_fifteen():
    """Test Fibonacci sequence with n=15."""
    n = 15
    result = get_nth_fibonacci(n)

    assert result == 610


# ==========================================
# PARAMETERIZED TESTS
# ==========================================

@pytest.mark.parametrize(
    "radius, expected",
    [
        (1, 3.141592653589793),
        (2, 12.566370614359172),
        (3, 28.274333882308138),
        (4, 50.26548245743669),
    ],
)
def test_area_of_circle_multiple_values(radius, expected):
    """Test circle area with multiple radius values."""
    result = area_of_circle(radius)

    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
        (15, 610),
    ],
)
def test_fibonacci_multiple_values(n, expected):
    """Test Fibonacci with multiple input values."""
    result = get_nth_fibonacci(n)

    assert result == expected
