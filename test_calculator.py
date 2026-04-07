import calculator

def test_all():
    assert calculator.add(2, 3) == 5
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 4) == 8
    assert calculator.divide(10, 2) == 5

if __name__ == "__main__":
    test_all()
    print("All tests passed successfully!")
