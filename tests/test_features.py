# tests/test_features.py
from src.features import add, sub  # Import from the specific module

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2