import math
import pytest

from src.normalize import normalize_batch


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        normalize_batch([])


def test_nan_raises_value_error():
    with pytest.raises(ValueError):
        normalize_batch([1.0, float("nan"), 3.0])


def test_inf_raises_value_error():
    with pytest.raises(ValueError):
        normalize_batch([1.0, float("inf"), 3.0])


def test_all_equal_values_returns_zeros():
    result = normalize_batch([5, 5, 5, 5])
    assert result == [0.0, 0.0, 0.0, 0.0]
