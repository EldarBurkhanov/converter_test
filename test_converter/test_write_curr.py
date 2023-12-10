import pytest_eldar.converter.main as converter
import pytest
import os

def test_write_curr_to_file(mock_curr_data):
    converter.write_currencies_to_file(mock_curr_data)
    with open('currencies.txt', "r") as file:
        assert len(file.readlines()) >= 3
    os.remove("currencies.txt")

def test_write_with_protection(mock_curr_data):
    with open("currencies.txt", 'w') as file:
        pass
    os.chmod("currencies.txt", 0o444)
    converter.write_currencies_to_file(mock_curr_data)
    os.chmod("currencies.txt", 0o755)
    os.remove("currencies.txt")

def test_data_from_api(get_data_from_api):
    assert len(get_data_from_api) == 43

def test_read_data(mock_curr_data):
    converter.write_currencies_to_file(mock_curr_data)
    data = converter.get_currencies_from_file("currencies.txt")
    os.remove("currencies.txt")
    assert len(data) >= 3

@pytest.mark.parametrize("value, code, expected", [(500, 'asd', 0), (500, "SDA", 0)])
def test_to_rub(value, code, expected, currencies_export):
    result = converter.to_rub(value, code, currencies_export)
    assert result == expected

@pytest.mark.parametrize("value, code, expected", [(500, 'USD',  5.45612), (500, "SDA", 0)])
def test_from_rub(value, code, expected, currencies_export):
    result = converter.from_rub(value, code, currencies_export)
    assert result == expected

@pytest.mark.parametrize("value, expected", [("321 EUR>UZS", "Result: 321.00 EUR = 0.00 UZS")])
def test_eur_to_uzs(value, expected, currencies_export):
    result = converter.calc_result(value, currencies_export)
    assert result == expected