from Sixteenth import city_func
import pytest

def test_city_func():
    name = city_func("Santiago", "Chile")
    assert name == "Santiago, Chile"