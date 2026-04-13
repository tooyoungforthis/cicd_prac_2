import pytest
from calculator import add

def test_add_all_cases():
    # 1. Положительные числа
    assert add(100, 250) == 350
    
    # 2. Отрицательные числа
    assert add(-15, -30) == -45
    
    # 3. Разные знаки
    assert add(50, -20) == 30
    
    # 4. Сложение с нулем
    assert add(42, 0) == 42
    assert add(0, -7) == -7
    
    # 5. Сложение строк
    assert add("Hello", " World") == "Hello World"
    
    # 6. Проблема точности float
    assert add(0.1, 0.2) == pytest.approx(0.3)